from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import re
# Create your models here.
class news(models.Model):
	title         = models.CharField(max_length=150, null=False)
	image         = models.ImageField(null=True,upload_to='NewsImages', height_field=None, width_field=None, max_length=100)
	thumbnail     = models.ImageField(null=True,blank=True,upload_to='NewsThumbnail', height_field=None, width_field=None, max_length=100)
	author        = models.CharField(max_length=50 , null=False)
	createdDate   = models.DateField(auto_now_add=True, auto_now=False)
	updatedDate   = models.DateField(auto_now_add=False, auto_now=True)
	context       = models.TextField(null=False)
	newsOrBlog    = models.BooleanField(default=True) # true represents news
	class Meta:
		ordering = ['-pk']

	def __str__(self):
		return self.title;
	def get_summary_text(self):
		no_tags = re.sub(re.compile('<.*?>'), ' ', self.context)
		no_tags = no_tags.replace('&nbsp;', ' ')
		trimmed = no_tags[0:512]
		if trimmed.rfind('.') != -1:
			return trimmed[:trimmed.rfind('.') + 1] + ('...' if trimmed.endswith('.') else '')
		else:
			return trimmed


class aboutUs(models.Model):
	context = models.TextField(null=False)


class introductionOfMembers(models.Model):
	name    = models.CharField(max_length=150, null=False)
	context = models.TextField(null=False)
	image   = models.ImageField(null=False,upload_to='introductionOfMembersImages',height_field=None,width_field=None,max_length=None)
	thumbnail     = models.ImageField(null=True,blank=True,upload_to='introductionOfMembersImagesThumbnail', height_field=None, width_field=None, max_length=100)
	class Meta:
		ordering = ['-pk']
	def __str__(self):
		return self.name;



class UiaiimageArchiveList(models.Model):
	image = models.ImageField(null=False,upload_to='UiaiimageArchiveList', height_field=None, width_field=None, max_length=100)
	thumbnail     = models.ImageField(null=True,blank=True,upload_to='UiaiimageArchiveListThumbnail', height_field=None, width_field=None, max_length=100)
	yearSemester     = models.ForeignKey('uiai',on_delete=models.CASCADE,null=False)
	class Meta:
		ordering = ['-pk']

class UiaiFiles(models.Model):
	file    = models.FileField(null=False)
	name    = models.CharField(max_length=150, null=False)
	yearSemester     = models.ForeignKey('uiai',on_delete=models.CASCADE,null=False)


class UiaiContext(models.Model):
	context = models.TextField(null=False)
	yearSemester     = models.ForeignKey('uiai',on_delete=models.CASCADE,null=False)

class uiai(models.Model):
	yearSemester     = models.CharField(null=False,max_length=30)
	class Meta:
		ordering = ['-pk']

	def __str__(self):
		return self.yearSemester	

class contests(models.Model):
	date         = models.DateField()
	problems    = models.FileField(null=False)
	judgesData   = models.FileField(null=False)
	rankingPhoto = models.ImageField(null=False,upload_to='contestsRankingPhoto',height_field=None,width_field=None,max_length=None)
	yearSemester     = models.ForeignKey('contestsYearSemester',on_delete=models.CASCADE,null=False)



		
class contestsYearSemester(models.Model):
	yearSemester     = models.CharField(null=False,max_length=30)
	def __str__(self):
		return self.yearSemester

class acmContestsTeams(models.Model):
	teamName    = models.CharField(null=False,max_length=50)
	image       = models.ImageField(null=False,upload_to='acmContestsTeamsImages',height_field=None,width_field=None,max_length=None)
	thumbnail     = models.ImageField(null=True,blank=True,upload_to='acmContestsTeamsImagesThumbnail', height_field=None, width_field=None, max_length=100)
	teamMembers = models.TextField(null=False)
	yearSemester    = models.ForeignKey('contestsYearSemester',on_delete=models.CASCADE,null=False)
	class Meta:
		ordering = ['-pk']

	def __str__(self):
		return self.teamName;




class studentContestsimageArchiveList(models.Model):
	image = models.ImageField(null=False,upload_to='studentContestsimageArchiveList', height_field=None, width_field=None, max_length=100)
	thumbnail     = models.ImageField(null=True,blank=True,upload_to='studentContestsimageArchiveListThumbnail', height_field=None, width_field=None, max_length=100)
	yearSemester    = models.ForeignKey('studentContests',on_delete=models.CASCADE,null=False)
	class Meta:
		ordering = ['-pk']


class studentContestsFiles(models.Model):
	file    = models.FileField(null=False)
	name    = models.CharField(max_length=150, null=False)
	yearSemester    = models.ForeignKey('studentContests',on_delete=models.CASCADE,null=False)


class studentContestsContext(models.Model):
	context = models.TextField(null=False)
	yearSemester    = models.ForeignKey('studentContests',on_delete=models.CASCADE,null=False)


class studentContests(models.Model):
	yearSemester     = models.CharField(null=False,max_length=30)
	def __str__(self):
		return self.yearSemester	






def resize_image(image_field, size, maintain_ratio=False):
    im = Image.open(image_field).convert('RGB')
    output = BytesIO()
    if maintain_ratio:
        ratio = min(size[0] / im.width, size[1] / im.height)
        size = (int(im.width * ratio), int(im.height * ratio))
    im = im.resize(size)
    im.save(output, format='JPEG', quality=100)
    output.seek(0)
    return InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % image_field.name.split('.')[0],
                                'image/jpeg', sys.getsizeof(output), None)

@receiver(models.signals.post_save, sender=news)

def make_thumbnail(sender, instance, created, **kwargs):
    if created:
        instance.thumbnail = resize_image(instance.image, size=(800, 600), maintain_ratio=False)
        instance.save()


@receiver(models.signals.post_save, sender=UiaiimageArchiveList)
def make_thumbnail(sender, instance, created, **kwargs):
    if created:
        instance.thumbnail = resize_image(instance.image, size=(800, 600), maintain_ratio=False)
        instance.save()



@receiver(models.signals.post_save, sender=studentContestsimageArchiveList)
def make_thumbnail(sender, instance, created, **kwargs):
    if created:
        instance.thumbnail = resize_image(instance.image, size=(800, 600), maintain_ratio=False)
        instance.save()  	




@receiver(models.signals.post_save, sender=acmContestsTeams)
def make_thumbnail(sender, instance, created, **kwargs):
    if created:
        instance.thumbnail = resize_image(instance.image, size=(800, 600), maintain_ratio=False)
        instance.save()


@receiver(models.signals.post_save, sender=introductionOfMembers)
def make_thumbnail(sender, instance, created, **kwargs):
    if created:
        instance.thumbnail = resize_image(instance.image, size=(800, 600), maintain_ratio=False)
        instance.save()


