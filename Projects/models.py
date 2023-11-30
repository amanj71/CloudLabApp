from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

#create your validators here
def validate_depth(depth_from, depth_to):
    if depth_to < depth_from:
        raise ValidationError(gettext_lazy("Bottom sample depth can't be smaller than top"))

# Create your models here.
class ProjectList(models.Model):
    user_company = models.CharField(max_length=255, default="BPI")
    project = models.CharField(max_length=255)
    client = models.CharField(max_length=255, blank=True)
    project_location_name = models.CharField(max_length=255, blank=True)
    geometry_nodes = models.FloatField(null=True, blank=True)
    project_description = models.TextField(blank=True)

    def __str__(self):
        return self.project

class Project(models.Model):
    division = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.division
    
    class Meta:
        ordering = ["division"]

class Division(models.Model):
    borehole = models.CharField(max_length=255)
    depth = models.FloatField()
    receive_date = models.DateField(null=True)

    def __str__(self):
        return self.borehole
    
class BoreHole(models.Model):
    sample_number = models.PositiveSmallIntegerField(null=True, blank=True)
    depth_from = models.FloatField()
    depth_to = models.FloatField(validators=[validate_depth])
    sample_types_choices = [('Bag', 'Bag'), ('SPT', 'SPT'), ('Shelby', "Shelby")]
    sample_type = models.CharField(max_length=8, choices=sample_types_choices, default='Bag')
    sample_description = models.TextField(blank=True)
