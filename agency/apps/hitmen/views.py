from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)

from django.views.generic.edit import (
    FormView
)

from . forms import (
    UserRegisterForm, 
    LoginForm,
    UserUpdateForm,
    UpdatePasswordForm,
)

from .models import User



class UserRegisterView(FormView):
    template_name = 'hitmen/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('hitmen_app:hitman-list')

    def form_valid(self, form):
        
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            status=form.cleaned_data['status'],
            manager=form.cleaned_data['manager'],
        )
        
        return super(UserRegisterView, self).form_valid(form)



class LoginUser(FormView):
    template_name = 'hitmen/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'hitmen_app:z-login'
            )
        )



class UserUpdateView(UpdateView):
    template_name = "hitmen/update.html"
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('hitmen_app:hitman-lista')


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('hitmen_app:hitman-lista')


class UpdatePasswordView(LoginRequiredMixin, FormView):
    # template_name = 'hitmen/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('hitmen_app:hitman-login')
    login_url = reverse_lazy('hitmen_app:hitman-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            email=usuario.email,
            password=form.cleaned_data['actual_password']
        )

        if user:
            new_password = form.cleaned_data['new_password']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


class UserListView(ListView):
    template_name = "hitmen/list.html"
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.system_users()
    