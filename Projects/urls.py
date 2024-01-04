from django.urls import path, include
from . import views

app_name = 'projects'

urlpatterns = [
    path("", views.projects, name="index" ),
    path("<int:proj_id>/", views.projectdetail, name="projectdetail"),
    path("<int:proj_id>/<int:div_id>/", views.divisiondetail, name="divisiondetail"),
    path("<int:proj_id>/<int:div_id>/<int:bh_id>", views.boreholedetail, name="boreholedetail"),
    path("api/", views.projectapi, name="project_api"),
    path("api/<int:proj_id>", views.projectdetail_api, name="projectdetail_api"),
    path("api/<int:proj_id>/<int:div_id>/", views.divisiondetail_api, name="divisiondetail_api"),
]