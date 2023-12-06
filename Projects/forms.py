from django import forms
from django.forms import formset_factory, modelformset_factory
from .models import BoreHole, Sample, Division

# write your ModelForms here
class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['division']

class BoreHoleForm(forms.ModelForm):
    class Meta:
        model = BoreHole
        fields = ['borehole', 'depth', 'receive_date']

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['sample_number', 'depth_from', 'depth_to', 'sample_type', 'sample_description']

# write formsets here
borehole_formset = formset_factory(BoreHoleForm, extra=1)
#sample_formset = formset_factory(SampleForm, extra=1)

sample_formset = modelformset_factory(Sample, fields=('sample_number', 'depth_from', 
                                                            'depth_to', 'sample_type', 'sample_description'), extra=1)
