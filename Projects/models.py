#from django.contrib.gis.db import models
from django.db import models

# Create your models here.
class ProjectList(models.Model):
    user_company = models.CharField(max_length=255, default="BPI")
    project = models.CharField(max_length=255)
    client = models.CharField(max_length=255, blank=True)
    project_location_name = models.CharField(max_length=255, blank=True)
    geometry_nodes = models.FloatField(null=True, blank=True)
    project_describtion = models.TextField(blank=True)

    def __str__(self):
        return self.project
