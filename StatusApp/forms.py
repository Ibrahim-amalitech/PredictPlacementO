from django import forms
from .models import Placement

class PlacementCreateForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = '__all__'