from django import forms
from .models import Photo

class AddPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'cover']