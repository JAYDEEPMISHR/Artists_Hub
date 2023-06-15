from django.db import models

# Create your models here.

class User(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=20,default='Artist')
	profile_pic=models.ImageField(upload_to="profile_pic/",default="")

	def __str__(self):
		return self.name+'-'+self.usertype

class Photo(models.Model):
	pic_name=models.CharField(max_length=100)
	date=models.DateTimeField()

	def __str__(self):
		return self.pic_name