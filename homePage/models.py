from django.db import models
 
# Create your models here.
class news(models.Model):
	title         = models.CharField(max_length=150, null=False)
	image         = models.ImageField(null=True,upload_to='img', height_field=None, width_field=None, max_length=100)
	author        = models.CharField(max_length=50 , null=False)
	createdDate   = models.DateField(auto_now_add=True, auto_now=False)
	updatedDate   = models.DateField(auto_now_add=False, auto_now=True)
	context       = models.TextField(null=False)
	newsOrBlog    = models.BooleanField(default=True) # true represents news

	def __str__(self):
		return self.title;
   	
class contactUs(models.Model):
	name    = models.CharField(max_length=50, null=False)
	email   = models.EmailField(null=False)
	context = models.TextField(null=False)

class aboutUs(models.Model):
	context = models.TextField(null=False)


class introductionOfMembers(models.Model):
		name    = models.CharField(max_length=150, null=False)
		context = models.TextField(null=False)
		image   = models.ImageField(null=False,upload_to='introductionOfMembersImg',height_field=None,width_field=None,max_length=None)



class imageArchive(models.Model):
	image = models.ImageField(null=False,upload_to='imageArchive', height_field=None, width_field=None, max_length=100)

class contests(models.Model):
	date   = models.DateField(auto_now_add=True, auto_now=False)
	file   = models.FileField(null=False)