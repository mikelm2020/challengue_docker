#
from django.urls import path

from . import views

app_name = "hitmen_app"

urlpatterns = [
    path(
        '', 
        views.LoginUser.as_view(),
        name='hitman-login',
    ),
    path(
        'hitmen/register/', 
        views.UserRegisterView.as_view(),
        name='hitmen-register',
    ),
    path(
        'hitmen/logout/', 
        views.LogoutView.as_view(),
        name='hitman-logout',
    ),
    path(
        'hitmen/update-password/<pk>/', 
        views.UpdatePasswordView.as_view(),
        name='hitman-update_password',
    ),
    path(
        'hitmen/update/<pk>/', 
        views.UserUpdateView.as_view(),
        name='hitman-update',
    ),
    path(
        'hitmen/delete/<pk>/', 
        views.UserDeleteView.as_view(),
        name='hitman-delete',
    ),
    path(
        'hitmen/lista/', 
        views.UserListView.as_view(),
        name='hitman-list',
    ),
]