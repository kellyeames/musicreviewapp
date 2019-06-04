from django.contrib import admin
from .models import GenreType, Album, Review

# Register your models here.
admin.site.register(GenreType)
admin.site.register(Album)
admin.site.register(Review)
