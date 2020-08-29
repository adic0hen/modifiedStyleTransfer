from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name= 'home'),
    path('add_content_photo/', AddContentPhotoView.as_view(), name='add_content_photo'),
    path('add_style_photo/', AddStylePhotoView.as_view(), name='add_style_photo'),
    path('test/', HomePageView.as_view(), name='test'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
    path('redirect/', redirect_view, name='redirect'),
    path('approve_style_transfer/', approveStyleTransfer, name='approve_style_transfer'),
    path('apply_style_transfer/', applyStyleTransfer, name='apply_style_transfer')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)