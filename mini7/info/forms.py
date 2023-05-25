from django import forms
from .models import Picture

class PictureForm(forms.Form):
    picture = forms.ModelChoiceField(queryset=Picture.objects.all().order_by('title'))
