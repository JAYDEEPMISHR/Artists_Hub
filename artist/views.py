from django.shortcuts import render,redirect
from .models import User,Photo,Video
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import random
import json
from django.utils import timezone
from django.http import JsonResponse

# Create your views here.

def index(request):
	return render(request,'artist-login.html')

def artist_register(request):
	if request.method=="POST":
		try:
			user=User.objects.all()
			if user.name == request.POST['name']: 
				msg="Username is already registered"
				return render(request,'artist-register.html',{'msg':msg})
			else:
				user=User.objects.get(email=request.POST['email'])
				msg="Email is already registered"
				return render(request,'artist-register.html',{'msg':msg})
		except:
			if request.POST['password'] == request.POST['cpassword']:
				user=User.objects.create(
						name=request.POST['name'],
						email=request.POST['email'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic']
					)
				msg="User registered successfully"
				return render(request,'artist-login.html',{'msg':msg})
			else:
				msg="Password and Confirm Password does not match"
				return render(request,'artist-register.html',{'msg':msg})
	else:
		return render(request,'artist-register.html')

def artist_login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password == request.POST['password']:
				request.session['email']=user.email
				request.session['name']=user.name
				request.session['profile_pic']=user.profile_pic.url
				return render(request,'homepage-artist.html')
			else:
				msg="Incorrect Password"
				return render(request,'artist-login.html',{'msg':msg})
		except:
			msg="Email is not registered"
			return render(request,'artist-register.html',{'msg':msg})
	else:
		return render(request,'artist-login.html')

def artist_home(request):
	pic= Photo.objects.all()
	return render(request,'homepage-artist.html',{'pic':pic})

def artist_logout(request):
	try:
		del request.session['email']
		del request.session['name']
		del request.session['profile_pic']
		return render(request,'artist-login.html')
	except:
		return render(request,'artist-login.html')

def artist_bio(request):
	return render(request,'artist-bio.html')

def artist_change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect(artist_logout)
			else:
				msg="New Password and Confirm Password does not match"
				return render(request,'artist-change-password.html',{'msg':msg})
		else:
			msg="Old Password does not match"
			return render(request,'artist-change-password.html',{'msg':msg})
	else:
		return render(request,'artist-change-password.html')

def add_image(request):
	if request.method=="POST":
		pic=Photo.objects.create(
			pic_name=request.POST['pic-name'],
			date=request.POST['date'],
			pic=request.FILES['file']
			)
		return render(request,'add-image.html',{'pic':pic})
	else:
		return render(request,'add-image.html')

def artist_add_video(request):
	if request.method=="POST":
		video=Video.objects.create(
			video_name=request.POST['video-name'],
			date=request.POST['date'],
			video=request.FILES['videofile']
			)
		return render(request,'artist-add-video.html',{'video':video})
	else:
		return render(request,'artist-add-video.html')

def artist_change_profile_pic(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":	
		try:
			user.profile_pic=request.FILE['profile_pic']
		except:
			pass
		user.save()
		msg="Profile-Pic change successfully"
		request.session['profile_pic']=user.profile_pic.url
		return render(request,'artist-change-profile-pic.html',{'user':user})
	else:
		return render(request,'artist-change-profile-pic.html',{'user':user})
