from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="projects_index" ),
    path("<int:project_id>", views.projectdetail, name="projects_projectdetail")
]