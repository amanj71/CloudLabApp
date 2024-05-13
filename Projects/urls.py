from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from . import views

app_name = 'projects'

# Asserting Routers
router = routers.SimpleRouter()
router.register('api/projects', views.ProjectViewSetAPI)





urlpatterns = [
    ## Your Actual App path
    path("", views.projects, name="index" ),
    path("<slug:slug>/", views.projectdetail, name="projectdetail"),
    path("division/<slug:slug>/", views.divisiondetail, name="divisiondetail"),
    path("borehole/<slug:slug>", views.boreholedetail, name="boreholedetail"),
    ## Your API PATH
    # path("api/", views.project_api, name="project_api"),
    # path("api/<int:proj_id>", views.projectdetail_api, name="projectdetail_api"),
    # path("api/<int:proj_id>/<int:div_id>/", views.divisiondetail_api, name="divisiondetail_api"),
]

urlpatterns += router.urls