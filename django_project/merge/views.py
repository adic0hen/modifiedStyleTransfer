from django.shortcuts import render
from .models import Photo
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import AddPhoto

from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('home')
    return response

class HomePageView(ListView):
    model = Photo
    template_name = 'merge/home.html'

class TestPageView(ListView):
    model = Photo
    template_name = 'merge/test.html'


class AddPhotoView(CreateView):
    model = Photo
    form_class = AddPhoto
    template_name = 'merge/add_photo.html'
    success_url = reverse_lazy('home')

class AboutPageView(ListView):
    model = Photo
    template_name = 'merge/about.html'

class GalleryPageView(ListView):
    model = Photo
    template_name = 'merge/gallery.html'