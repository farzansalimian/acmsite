# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView , ListView , CreateView, TemplateView
from django.shortcuts import render
from django.views.generic.list import ListView
from .forms import buyersForm
from .models import Buyers
from django.contrib.messages.views import SuccessMessageMixin

#def book_id_user_name(request):
#	now = datetime.datetime.now()
	#html = '{ "status": status_code }' 
	#return HttpResponse(html)
class AskSpeed(TemplateView):
	template_name='askSpeed.html'
class lowSpeedView(TemplateView):
	template_name='lowSpeed.html'
class MtpluslowSpeedView(TemplateView):
	template_name='mtpluslowSpeed.html'

class HomePage(TemplateView):
	template_name='home.html'
	
class ReviewS9(TemplateView):
	template_name = "ReviewS9.html"

class ReviewS9Plus(TemplateView):
	template_name = "ReviewS9Plus.html"


class DetailsS9(TemplateView):
	template_name = "DetailsS9.html"

class DetailsS9Plus(TemplateView):
	template_name = "DetailsS9Plus.html"


class BuyerView(SuccessMessageMixin, CreateView):
	def get(self, request, *args, **kwargs):
		
		return render(request, 'buyers.html', {'form': buyersForm()})
	form_class = buyersForm
	template_name = 'buyers.html'
	success_url = '/'
	success_message = "ثبت نام با موفقیت انجام شد"


class mtplusView(TemplateView):
	template_name='mtplus.html'