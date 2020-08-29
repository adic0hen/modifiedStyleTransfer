from django.shortcuts import render
from .models import ContentPhoto, StylePhoto
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import AddContentPhotoForm, AddStylePhotoForm
from neural_style_logic import neural_style

from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('home')
    return response

def home(request):
    context = {
        'content_images': ContentPhoto.objects.all(),
        'style_images': StylePhoto.objects.all(),
        'last_content':  ContentPhoto.objects.last(),
        'last_style':  StylePhoto.objects.last()
    }
    return render(request, 'merge/home.html', context=context)

def applyStyleTransfer(request):
    contentDir = "--content_img_dir ./"
    styleDir = "--style_imgs_dir ./"
    contentData = "--content_img {}".format(ContentPhoto.objects.last().cover.path)
    styleData = "--style_imgs {}".format(StylePhoto.objects.last().cover.path)
    print("APPLYING STYLE TRANSFER THROUGH THE WEBSITE")
    styleTransferRequest = neural_style.DefaultRequest(contentDir=contentDir, styleDir=styleDir, contentData=contentData, styleData=styleData)
    args = styleTransferRequest.getRequestArgs()
    print(str(args))
    neural_style.runInternalWithArguments(args)
    return redirect('gallery')

def approveStyleTransfer(request):
    context = {
        'content_images': ContentPhoto.objects.all(),
        'style_images': StylePhoto.objects.all(),
        'last_content':  ContentPhoto.objects.last(),
        'last_style':  StylePhoto.objects.last()
    }
    return render(request, 'merge/approve_style_transfer.html', context=context)

class HomePageView(ListView):
    model = StylePhoto
    template_name = 'merge/home.html'

class TestPageView(ListView):
    model = ContentPhoto
    template_name = 'merge/test.html'


class AddContentPhotoView(CreateView):
    model = ContentPhoto
    form_class = AddContentPhotoForm
    template_name = 'merge/add_content_photo.html'
    success_url = reverse_lazy('add_style_photo')

class AddStylePhotoView(CreateView):
    model = StylePhoto
    form_class = AddStylePhotoForm
    template_name = 'merge/add_style_photo.html'
    success_url = reverse_lazy('approve_style_transfer')

class AboutPageView(ListView):
    model = ContentPhoto
    template_name = 'merge/about.html'

class GalleryPageView(ListView):
    model = ContentPhoto
    template_name = 'merge/gallery.html'
