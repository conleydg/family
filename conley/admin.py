from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Movie, Tag, People

class MovieAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)
