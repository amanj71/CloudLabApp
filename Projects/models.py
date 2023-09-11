from django.contrib.gis.db import models
#from django.db import models

# Create your models here.
class ProjectList(models.Model):
    user_company = models.CharField(max_length=255, default="BPI")
    project = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    project_location_name = models.CharField(max_length=255)
    geometry_nodes = models.GeometryField(dim=3)
    project_describtion = models.TextField()
