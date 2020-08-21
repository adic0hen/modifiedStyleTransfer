from . import views
from .views import HomePageView, AddPhotoView, redirect_view, AboutPageView, GalleryPageView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name= 'home'),
    path('add_photo/', AddPhotoView.as_view(), name='add_photo'),
    path('test/', HomePageView.as_view(), name='test'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
    path('redirect/', redirect_view, name='redirect')
]