from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'login.html')

def register(request):
	return render(request,'register.html')

def home(request):
	return render(request,'sidebar.html')

def dashboard(request):
	return render(request,'dashboard.html')