from django.urls import path, include
from . import views

app_name = 'projects'

urlpatterns = [
    path("", views.index, name="index" ),
    path("<int:proj_id>/", views.projectdetail, name="projectdetail"),
    path("api/", views.project_api, name="project_api"),
    path("api/<int:proj_id>", views.project_detail_api, name="projectdetail_api"),
]