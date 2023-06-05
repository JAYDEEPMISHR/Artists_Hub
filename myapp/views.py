from django.shortcuts import render,redirect
from .models import User,Video

# Create your views here.

def index(request):
	return render(request,'login.html')

def register(request):
	if request.method=="POST":
		try:
			user=User.objects.all()
			if user.name == request.POST['name']: 
				msg="Username is already registered"
				return render(request,'register.html',{'msg':msg})
			else:
				user=User.objects.get(email=request.POST['email'])
				msg="Email is already registered"
				return render(request,'register.html',{'msg':msg})
		except:
			if request.POST['password'] == request.POST['cpassword']:
				user=User.objects.create(
						usertype=request.POST['usertype'],
						name=request.POST['name'],
						email=request.POST['email'],
						password=request.POST['password'],
					)

				msg="User registered successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password and Confirm Password does not match"
				return render(request,'register.html',{'msg':msg})
	else:
		return render(request,'register.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password == request.POST['password']:
				if user.usertype=="User":
					request.session['email']=user.email
					request.session['name']=user.name
					request.session['usertype']=user.usertype
					request.session['profile_pic']=user.profile_pic.url
					return render(request,'dashboard.html')

				elif user.usertype=="Artists":
					request.session['email']=user.email
					request.session['name']=user.name
					request.session['usertype']=user.usertype
					request.session['profile_pic']=user.profile_pic.url
					return render(request,'artist-homepage.html')

				else:
					request.session['email']=user.email
					request.session['name']=user.name
					request.session['usertype']=user.usertype
					request.session['profile_pic']=user.profile_pic.url
					return render(request,'dashboard.html')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email is not registered"
			return render(request,'registration.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['name']
		del request.session['usertype']
		del request.session['profile_pic']
		return redirect('index')
	except:
		return render(request,'login.html')



def home(request):
	return render(request,'sidebar.html')

def dashboard(request):
	return render(request,'dashboard.html')

def booking(request):
	return render(request,'book-appointment.html')

def artist_profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.usertype=="Artists":
			user.name=request.POST['name']
			user.save()
			request.session['name']=user.name
			return render(request,'artist-profile.html',{'user':user})
		else:
			pass
	else:
		return render(request,'edit-artist-profile.html')

def artist_dashboard(request):
	return render(request,'artist-homepage.html')

def add_photos_video(request):
	return render(request,'add-photos-video.html')