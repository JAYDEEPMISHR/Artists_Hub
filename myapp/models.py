from django.db import models

# Create your models here.

class User(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=20,default='User')
	profile_pic=models.ImageField(upload_to="profile_pic/",default="")

	def __str__(self):
		return self.name+'-'+self.usertype

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)