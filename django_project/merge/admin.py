from django.contrib import admin

# Register your models here.

from .models import ContentPhoto, StylePhoto, ResultPhoto

admin.site.register(ContentPhoto)
admin.site.register(StylePhoto)
admin.site.register(ResultPhoto)