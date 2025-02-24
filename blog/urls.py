from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        'vehicles-projects/',
        views.VehicleProjectList.as_view(),
        name='project_list'
    ),
    path(
        'vehicles-projects/create/',
        login_required(views.create_vehicle_project),
        name='project_create'
    ),
    path(
        'vehicles-projects/<slug:slug>/',
        views.vehicle_project_detail,
        name='project_detail'
    ),
    path(
        'vehicles-projects/<slug:slug>/edit/',
        login_required(views.edit_vehicle_project),
        name='edit_vehicle_project'
    ),
    path(
        'vehicles-projects/<slug:slug>/delete/',
        login_required(views.VehicleProjectDelete.as_view()),
        name='project_delete'
    ),
    path(
        'vehicles-projects/<slug:slug>/like/',
        login_required(views.like_project),
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
    ),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>/',
        views.comment_delete,
        name='comment_delete'
    ),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>/',
        views.comment_edit,
        name='comment_edit'
    )
]
