from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.utils.deconstruct import deconstructible
from django.conf import settings
# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    logged_in = models.BooleanField(default=False)
    #img = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(settings.MEDIA_ROOT, 'upload')))    
    
    def __str__ (self):
    	return self.last_name
