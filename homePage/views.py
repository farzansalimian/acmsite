from django.shortcuts import render
from django.views.generic import DetailView as DV
from django.views.generic.list import ListView as LV
from .models import news, aboutUs, introductionOfMembers, contests, imageArchive, contactUs
from django.views.generic import CreateView as CV
from .forms import userContactUsForm
# Create your views here.
class homepage(LV):
	models=news
	template_name='newsListView_list.html'
	queryset=news.objects.all()

class showDetailNews(DV):
	models=news
	template_name='newsDetailView_list.html'
	def get_queryset(self):
		queryset=news.objects.filter(pk=self.kwargs.get("pk"))
		return queryset

class aboutUsView(LV):
	template_name='aboutUs.html'
	queryset=aboutUs.objects.all()
	def get_context_data(self,**kwargs):
		context = super(aboutUsView,self).get_context_data(**kwargs)
		context['introductionOfMembers'] = introductionOfMembers.objects.all()
		context['aboutUs'] = aboutUs.objects.all()
		return context
class contestsList(LV):
	models=contests
	template_name='contestsList.html'
	queryset=contests.objects.all()

class imageArchiveList(LV):
	models = imageArchive
	template_name ='imageArchive.html'
	queryset = imageArchive.objects.all()
class contactUsViewUser(CV):
	form_class = userContactUsForm
	template_name = 'contactUsView.html'
	success_url = '/home'
	models = contactUs
	