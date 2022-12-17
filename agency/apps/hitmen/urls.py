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
        'register/', 
        views.UserRegisterView.as_view(),
        name='hitmen-register',
    ),
    path(
        'logout/', 
        views.LogoutView.as_view(),
        name='hitman-logout',
    ),
    path(
        'hitmen/', 
        views.UserListView.as_view(),
        name='hitman-list',
    ),
    path(
        'hitmen/<int:pk>/', 
        views.UserDetailView.as_view(),
        name='hitman-detail',
    ),
]