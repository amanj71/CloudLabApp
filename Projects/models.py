from typing import Iterable
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils.translation import gettext_lazy
from .utils import generate_unique_slug, generate_random_string

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
    slug = models.SlugField(default='-',)

    def __str__(self):
        return self.project
    
    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(f"{self.project}-{self.project_location_name}") != self.slug:
                self.slug = generate_unique_slug(Project, self.project, self.project_location_name)
        else:  # create
            self.slug = generate_unique_slug(Project, self.project, self.project_location_name)
        super(Project, self).save(*args, **kwargs)
    
class Division(models.Model):
    division = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(default='-')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='project_related', null=True)
    
    class Meta:
        ordering = ["division"]
    
    def __str__(self):
        return self.division
    
    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(f"{self.project.project}-{self.division}") != self.slug:
                self.slug = generate_unique_slug(Division, self.project.project, self.division)
        else:  # create
            self.slug = generate_unique_slug(Division, self.project.project, self.division)
        super(Division, self).save(*args, **kwargs)
    

class BoreHole(models.Model):
    borehole = models.CharField(max_length=255, null=True, blank=True)
    depth = models.FloatField(null=True)
    receive_date = models.DateField(null=True)
    division = models.ForeignKey(Division, on_delete=models.PROTECT, related_name='division_related', null=True, blank=True)
    slug = models.SlugField(default='-')

    def __str__(self):
        return self.borehole
    
    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(f"{self.division.division}-{self.borehole}-{self.depth}") != self.slug:
                self.slug = generate_unique_slug(BoreHole, self.division.division, self.borehole, str(self.depth))
        else:  # create
            self.slug = generate_unique_slug(BoreHole, self.division.division, self.borehole, str(self.depth))    
        super(BoreHole, self).save(*args, **kwargs)
    
class Sample(models.Model):
    sample_number = models.PositiveSmallIntegerField(null=True, blank=True)
    depth_from = models.FloatField()
    depth_to = models.FloatField()
    sample_types_choices = [('Bag', 'Bag'), ('SPT', 'SPT'), ('Shelby', "Shelby")]
    sample_type = models.CharField(max_length=8, choices=sample_types_choices, default='Bag')
    sample_description = models.TextField(blank=True)
    random_string = models.CharField(max_length=10, blank=True, editable=False, default=generate_random_string(10))
    borehole = models.ForeignKey(BoreHole, on_delete=models.PROTECT, related_name='borehole_related', null=True, blank=True)
    slug = models.SlugField(default='-')

    class Meta:
        ordering = ['depth_from']
    
    def __str__(self):
        return str(self.sample_number)
    
    def clean(self):
        """
        Custom validation to check if sample_number is unique and depth_to is greater than depth_from.
        """
        if self.sample_number is not None:
            existing_samples = Sample.objects.exclude(pk=self.pk)
            if existing_samples.filter(sample_number=self.sample_number, borehole__id=self.borehole.id).exists():
                raise ValidationError(f"Sample number {self.sample_number} is already used.")
        if self.depth_to < self.depth_from:
            raise ValidationError(
                {"depth_to": gettext_lazy("Bottom sample depth can't be smaller than top")}
            )
    
    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(f"{self.borehole.division.project.project}-{self.borehole.borehole}-{self.depth_from}-{self.depth_to}-{self.random_string}") != self.slug:
                self.slug = generate_unique_slug(Sample, self.borehole.division.project.project,
                         self.borehole.borehole, str(self.depth_from), str(self.depth_to), self.random_string)
        else:  # create
            self.slug = generate_unique_slug(Sample, self.borehole.division.project.project,
                         self.borehole.borehole, str(self.depth_from), str(self.depth_to), self.random_string)
        super(Sample, self).save(*args, **kwargs)

    