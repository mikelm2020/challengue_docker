
from django.urls import path

from apps.hits import views

app_name = "hits_app"

urlpatterns = [
    path(
        'hits/create/', 
        views.HitRegisterView.as_view(),
        name='hit-register',
    ),
    path(
        'hits/bulk/', 
        views.HitAddBulkView.as_view(),
        name='hit-bulk',
    ),
    path(
        'hits/', 
        views.HitListView.as_view(),
        name='hit-list',
    ),
    path(
        'hits/<int:pk>/', 
        views.HitDetailView.as_view(),
        name='hit-detail',
    ),
]