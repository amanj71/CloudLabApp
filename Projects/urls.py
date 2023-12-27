from django.urls import path, include
from . import views

app_name = 'projects'

urlpatterns = [
    path("", views.projects, name="index" ),
    path("<int:proj_id>/", views.projectdetail, name="projectdetail"),
    #path("<int:proj_id>/<int:div_id/>", views.divisiondetail, name="divisiondetail"),
    path("api/", views.project_api, name="project_api"),
    path("api/<int:proj_id>", views.project_detail_api, name="projectdetail_api"),
]