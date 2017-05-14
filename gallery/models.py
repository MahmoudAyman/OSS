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

class Projects(models.Model):
    title = models.CharField(primary_key=True, max_length=200)
    desc = models.CharField(max_length=400, default="")
    img = models.CharField(max_length=200, default="")
    contentVid=models.CharField(max_length=400, default="")
    contentImg = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(settings.MEDIA_ROOT, 'upload')))
    contentText=models.TextField()
    def __str__ (self):
    	return self.title


