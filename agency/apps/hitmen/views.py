from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DetailView
from django.views.generic.edit import FormView

from apps.hitmen.forms import LoginForm, UserRegisterForm
from apps.hitmen.models import User
from apps.hitmen.mixins import (
    AdminAndManagersPermissionMixin,
    AutheticatedPermissionMixin,
)


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


class UserDetailView(AutheticatedPermissionMixin, DetailView):
    model = User
    template_name = "hitmen/detail.html"


class LoginUser(FormView):
    template_name = "hitmen/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("hitmen_app:hitman-list")

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data["email"], password=form.cleaned_data["password"]
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):
    # success_url = "/"
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect("/")


# class UserListView(MultipleObjectMixin, ListView):
#     # paginate_by = 5
#     template_name = "hitmen/list.html"
#     context_object_name = "hitmen"
#     ordering = "name"

#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return User.objects.hitmen_in_system()
#         else:
#             return User.objects.hitmen_by_manager(self.request.user)


class UserListView(AdminAndManagersPermissionMixin, ListView):
    template_name = "hitmen/list.html"
    context_object_name = "hitmen"
    paginate_by = 5

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.hitmen_by_manager(self.request.user.id)

        # if self.request.user.manager 0:
        #     return User.objects.hitmen_by_manager(request.user)
        # else:
        #     return User.objects.hitmen_in_system()


# class UserUpdateView(UpdateView):
#     template_name = "hitmen/update.html"
#     model = User
#     form_class = UserUpdateForm
#     success_url = reverse_lazy('hitmen_app:hitman-lista')


# class UserDeleteView(DeleteView):
#     model = User
#     success_url = reverse_lazy('hitmen_app:hitman-lista')


# class UpdatePasswordView(LoginRequiredMixin, FormView):
#     # template_name = 'hitmen/update.html'
#     form_class = UpdatePasswordForm
#     success_url = reverse_lazy('hitmen_app:hitman-login')
#     login_url = reverse_lazy('hitmen_app:hitman-login')

#     def form_valid(self, form):
#         usuario = self.request.user
#         user = authenticate(
#             email=usuario.email,
#             password=form.cleaned_data['current_password']
#         )

#         if user:
#             new_password = form.cleaned_data['new_password']
#             usuario.set_password(new_password)
#             usuario.save()

#         logout(self.request)
#         return super(UpdatePasswordView, self).form_valid(form)
