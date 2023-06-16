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
	pic=models.ImageField(upload_to="upload_images/", default=True)

	def __str__(self):
		return self.pic_name

class Video(models.Model):
	video=models.FileField(upload_to="videos/")
	date=models.DateTimeField()
	video_name=models.CharField(max_length=200)

	def __str__(self):
		return self.video_name