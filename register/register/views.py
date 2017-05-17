from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from register.models import *
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
import os 

def form(request):
	return render(request, 'register/form.html')

def logIn(request):
	name = request.POST['username'].split(" ")[0]
	pwd = request.POST['password']
	context={}
	try:
		usr = Member.objects.get(first_name=name)
	except (KeyError, Member.DoesNotExist):
		context['errors']=True
		return render(request, "register/form.html", context)
	else:
		if (usr.pwd == pwd):
			usr.logged_in=True
			usr.save()
			request.session['member_id'] = usr.id
			request.session.set_expiry(0)
			return HttpResponseRedirect(reverse('landing:index'))
		else: 
			return render(request, "register/form.html", context)

def checkAuth (request):
	try:
		m_id=request.session['member_id']
	except KeyError:
		return False
	return m_id

def logOut(request):
	try:
		m_id=request.session['member_id']
	except KeyError:
		return render(request, "register/index.html")
	else:
		m= Member.objects.get(pk=m_id)
		m.logged_in=False
		m.save()
		del request.session['member_id']
		return render(request, "register/index.html")

def signUp(request):
	fname = request.POST['firstname']
	lname = request.POST['lastname']
	mail = request.POST['emailsignup']
	password = request.POST['passwordsignup']
	pwd2 = request.POST['passwordsignup_confirm']
	#u_img = request.FILES['img']
	context={}

	if (password != pwd2):
		context['wrong']=True
		return render(request, "register/form.html", context)
	else:
		mem = Member.objects.create(first_name=fname, last_name=lname, email=mail, pwd=password, logged_in=True,)
		request.session['member_id'] = mem.id
		request.session.set_expiry(0)
		#mem.img=(u_img)
		mem.save()
		# file ,ext  = os.path.splitext(mem.img.path)
		# size = (60,60)
		# mask = Image.new('L', size, 0)
		# draw = ImageDraw.Draw(mask) 
		# draw.ellipse((0, 0) + size, fill=255)
		# im = Image.open(mem.img.path)
		# output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
		# output.putalpha(mask)
		# output.save(file + "-thumbnail"+".png")
		return HttpResponseRedirect(reverse('landing:index'))
