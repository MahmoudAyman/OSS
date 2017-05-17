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
	return render(request, 'members/index.html')
