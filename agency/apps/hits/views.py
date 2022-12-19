from apps.hitmen.mixins import (
    AdminAndManagersPermissionMixin,
    AutheticatedPermissionMixin,
)
from apps.hits.forms import HitAddForm, HitAddBulkForm, HitUpdateForm
from apps.hits.models import Hits
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import FormView
from apps.hitmen.managers import UserManager
from apps.hitmen.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy

class HitRegisterView(AdminAndManagersPermissionMixin, FormView):
    template_name = "hits/register.html"
    form_class = HitAddForm
    success_url = reverse_lazy("hits_app:hit-list")

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(user=self.request.user, **self.get_form_kwargs())

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        
        return super(HitRegisterView, self).form_valid(form)




class HitAddBulkView(AdminAndManagersPermissionMixin, FormView):
    template_name = "hits/bulk.html"
    form_class = HitAddBulkForm
    success_url = "/hits"

    def form_valid(self, form):

        Hits.objects.create_hit(
            form.cleaned_data["assigne"],
            form.cleaned_data["description"],
            form.cleaned_data["target_name"],
            form.cleaned_data["status"],
            form.cleaned_data["creator"],
        )

        return super(HitAddBulkView, self).form_valid(form)


class HitDetailView(AutheticatedPermissionMixin, UpdateView):
    model = Hits
    template_name = "hits/detail.html"
    success_url = reverse_lazy("hits_app:hit-list")
    form_class = HitUpdateForm

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()

    #     return super().post(request, *args, **kwargs)
    
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.save()

    #     return super(HitDetailView, self).form_valid(form)


class HitListView(AutheticatedPermissionMixin, ListView):
    template_name = "hits/list.html"
    context_object_name = "hits"
    paginate_by = 5

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Hits.objects.all()
        else:
            return Hits.objects.hits_of_hitmen(self.request.user.id)
