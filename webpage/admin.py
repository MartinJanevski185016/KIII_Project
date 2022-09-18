from django.contrib import admin
from .models import Youtube
from embed_video.admin import AdminVideoMixin

# Register your models here.
class YoutubeAdmin(AdminVideoMixin, admin.ModelAdmin):
    display = ('url')

admin.site.register(Youtube, YoutubeAdmin)