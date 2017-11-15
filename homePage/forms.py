from django import forms
from .models import news
class adminAddNews(forms.ModelForm):
	class Meta:
		model = news
		fields=['title','image','author','context'] 

