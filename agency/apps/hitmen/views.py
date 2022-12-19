from apps.hitmen.forms import LoginForm, UserRegisterForm, UserUpdateForm
from apps.hitmen.mixins import (
    AdminAndManagersPermissionMixin,
    AutheticatedPermissionMixin,
)
from apps.hitmen.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View, UpdateView
from django.views.generic.edit import FormView


class UserRegisterView(FormView):
    template_name = "hitmen/register.html"
    form_class = UserRegisterForm
    success_url = "/"

    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data["name"],
            form.cleaned_data["email"],
            form.cleaned_data["password"],
        )

        return super(UserRegisterView, self).form_valid(form)


class UserDetailView(AutheticatedPermissionMixin, UpdateView):
    model = User
    template_name = "hitmen/detail.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("hitmen_app:hitman-list")



class LoginUser(FormView):
    template_name = "hitmen/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("hits_app:hit-list")

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data["email"], password=form.cleaned_data["password"]
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect("/")


class UserListView(AdminAndManagersPermissionMixin, ListView):
    template_name = "hitmen/list.html"
    context_object_name = "hitmen"
    paginate_by = 5

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.hitmen_by_manager(self.request.user.id)
