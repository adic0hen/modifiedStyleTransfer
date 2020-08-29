from django import forms
from .models import ContentPhoto
from .models import StylePhoto

class AddContentPhotoForm(forms.ModelForm):
    class Meta:
        model = ContentPhoto
        fields = ['cover']



class AddStylePhotoForm(forms.ModelForm):
    class Meta:
        model = StylePhoto
        fields = ['cover']