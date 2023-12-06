from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

#create your validators here
def validate_depth(self):
    if self.depth_to < self.depth_from:
        raise ValidationError(gettext_lazy("Bottom sample depth can't be smaller than top"))

# Create your models here.
class Project(models.Model):
    user_company = models.CharField(max_length=255, default="BPI")
    project = models.CharField(max_length=255)
    client = models.CharField(max_length=255, blank=True)
    project_location_name = models.CharField(max_length=255, blank=True)
    geometry_nodes = models.FloatField(null=True, blank=True)
    project_description = models.TextField(blank=True)

    def __str__(self):
        return self.project

class Division(models.Model):
    division = models.CharField(max_length=255, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_related', null=True)

    def __str__(self):
        return self.division
    
    class Meta:
        ordering = ["division"]

class BoreHole(models.Model):
    borehole = models.CharField(max_length=255, null=True, blank=True)
    depth = models.FloatField(null=True)
    receive_date = models.DateField(null=True)
    division = models.ForeignKey(Division, on_delete=models.PROTECT, related_name='division_related', null=True, blank=True)

    def __str__(self):
        return self.borehole
    
class Sample(models.Model):
    sample_number = models.PositiveSmallIntegerField(null=True, blank=True)
    depth_from = models.FloatField()
    depth_to = models.FloatField()
    sample_types_choices = [('Bag', 'Bag'), ('SPT', 'SPT'), ('Shelby', "Shelby")]
    sample_type = models.CharField(max_length=8, choices=sample_types_choices, default='Bag')
    sample_description = models.TextField(blank=True)
    borehole = models.ForeignKey(BoreHole, on_delete=models.PROTECT, related_name='borehole_related', null=True, blank=True)

    class Meta:
        ordering = ['depth_from']
    
    def clean(self):
        super().clean()
        if self.depth_to < self.depth_from:
            raise ValidationError(
                {"depth_to": gettext_lazy("Bottom sample depth can't be smaller than top")}
            )

    def __str__(self):
        return self.sample_number

    