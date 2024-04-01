from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = 'projects'

urlpatterns = [
    path("", views.projects, name="index" ),
    path("<slug:slug>/", views.projectdetail, name="projectdetail"),
    path("division/<slug:slug>/", views.divisiondetail, name="divisiondetail"),
    path("borehole/<slug:slug>", views.boreholedetail, name="boreholedetail"),
    path("api/", views.project_api, name="project_api"),
    path("api/<int:proj_id>", views.projectdetail_api, name="projectdetail_api"),
    path("api/<int:proj_id>/<int:div_id>/", views.divisiondetail_api, name="divisiondetail_api"),
]