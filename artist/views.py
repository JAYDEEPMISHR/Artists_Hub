from django.shortcuts import render
from .models import User

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
	return render(request,'artist-login.html')

def artist_home(request):
	return render(request,'homepage-artist.html')