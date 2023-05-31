from django.shortcuts import render
from .models import User

# Create your views here.

def index(request):
	return render(request,'login.html')

def register(request):
	if request.method=="POST":
		try:
			user=User.objects.all()
			if user.name == request.POST['name']: 
				msg="Email already registered"
				return render(request,'register.html',{'msg':msg})
			else:
				user=User.objects.get(name=request.POST['name'])
				msg="Username is already registered"
				return render(request,'register.html',{'msg':msg})
		except:
			if request.POST['password'] == request.POST['cpassword']:
				user=User.objects.create(
						name=request.POST['name'],
						email=request.POST['email'],
						password=request.POST['password']
					)

				msg="User registered successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password and Confirm Password does not match"
				return render(request,'register.html',{'msg':msg})
	else:
		return render(request,'register.html')

# def login(request):
# 	if request.method=="POST":
# 		try:
# 			user=User.objects.get(email=request.POST['email'])
# 			if user.password == request.POST['password']:


def home(request):
	return render(request,'sidebar.html')

def dashboard(request):
	return render(request,'dashboard.html')