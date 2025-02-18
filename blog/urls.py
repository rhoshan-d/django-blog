from . import views
from django.urls import path

urlpatterns = [
    path(
        'vehicles-projects/',
        views.VehicleProjectList.as_view(),
        name='project_list'
    ),
    path(
        'vehicles-projects/create/',
        views.create_vehicle_project,
        name='project_create'
    ),
    path(
        'vehicles-projects/<slug:slug>/',
        views.vehicle_project_detail,
        name='project_detail'
    ),
    path(
        'vehicles-projects/<slug:slug>/edit/',
        views.edit_vehicle_project,
        name='edit_vehicle_project'
    ),
    path(
        'vehicles-projects/<slug:slug>/delete/',
        views.VehicleProjectDelete.as_view(),
        name='project_delete'
    ),
    path(
        'vehicles-projects/<slug:slug>/like/',
        views.like_project,
        name='like_project'
    ),
    path(
        "",
        views.PostList.as_view(),
        name='home'
    ),
    path(
        '<slug:slug>/',
        views.post_detail,
        name='post_detail'
    )
]
