from django import forms
from .models import news, contactUs
class adminAddNews(forms.ModelForm):
	class Meta:
		model = news
		fields=['title','image','author','context'] 

class userContactUsForm(forms.ModelForm):
	class Meta:
		model = contactUs
		fields =['name','email','context']