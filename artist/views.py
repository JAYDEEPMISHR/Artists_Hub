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
	return render(request,'homepage-artist.html')

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