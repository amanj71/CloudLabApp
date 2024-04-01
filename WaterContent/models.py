from django.db import models
from Projects.models import Project, Division, BoreHole, Sample

# Create your models here.
class WaterContent(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, blank=True, null=True)
    borehole = models.ForeignKey(BoreHole, on_delete=models.CASCADE, blank=True, null=True)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, editable=True)
    weight_tin = models.DecimalField(max_digits=10, decimal_places=2)
    wet_weight_tin_soil = models.DecimalField(max_digits=10, decimal_places=2)
    dry_weight_tin_soil = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.project.project}-{self.borehole.borehole}-Sample: {self.sample.sample_number} - {self.sample.depth_from}m"
    
    def get_sample_depth(self):
        return str(self.sample.depth_from)
    
    def get_sample_slug(self):
        return self.sample.slug

class AjaxTest(models.Model):
    name = models.CharField(max_length=50)   
    email = models.EmailField()   
    text = models.CharField(max_length=100)  

    def __str__(self):
        return f"{self.name}-{self.email}**"
    