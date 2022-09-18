from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
# Create your models here.
class Youtube(models.Model):
    url = EmbedVideoField()



