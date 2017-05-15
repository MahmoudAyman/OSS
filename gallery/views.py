from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from gallery.models import *
from django.urls import reverse
import os 
from PIL import Image
# Create your views here.

def index (request):
	li = Projects.objects.all()
	# try:
	# 	request.session['member_id']
	# except KeyError:
	# 	log=False
	# else:
	# 	log=True 
	context={'courses':li}
	return render(request, 'gallery/index.html',context)

