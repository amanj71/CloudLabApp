from django import forms
from .models import WaterContent
from Projects.models import Division, BoreHole

class WaterContentForm(forms.ModelForm):
    class Meta:
        model = WaterContent
        fields = ['project', 'division', 'borehole']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["division"].queryset = Division.objects.none()