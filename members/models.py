from __future__ import unicode_literals
import PIL
from django.db import models
from django.forms import ModelForm
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.conf import settings
# Create your models here.

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    logged_in = models.BooleanField(default=False)
    img = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(settings.MEDIA_ROOT, 'upload')))    
    # upload_date=models.DateTimeField(auto_now_add =True)

    def __str__ (self):
        return self.last_name
