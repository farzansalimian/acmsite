# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView , ListView , CreateView, TemplateView
from django.shortcuts import render
from django.views.generic.list import ListView
from .forms import buyersForm, ContactForm
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

class ReviewS9PlusLowSpeed(TemplateView):
	template_name = "ReviewS9PlusLowSpeed.html"
class ReviewS9LowSpeed(TemplateView):
	template_name = "ReviewS9LowSpeed.html"

class ReviewS9Plus(TemplateView):
	template_name = "ReviewS9Plus.html"


class DetailsS9(TemplateView):
	template_name = "DetailsS9.html"

class DetailsS9Plus(TemplateView):
	template_name = "DetailsS9Plus.html"

class DetailsS9LowSpeed(TemplateView):
	template_name = "DetailsS9LowSpeed.html"

class DetailsS9PlusLowSpeed(TemplateView):
	template_name = "DetailsS9PlusLowSpeed.html"

class BuyerView(SuccessMessageMixin, CreateView):
	def get(self, request, *args, **kwargs):
		
		return render(request, 'buyers.html', {'form': buyersForm()})
	form_class = buyersForm
	template_name = 'buyers.html'
	success_url = '/'
	success_message = "ثبت نام با موفقیت انجام شد"
class BuyerViewLowSpeed(SuccessMessageMixin, CreateView):
	def get(self, request, *args, **kwargs):
		
		return render(request, 'buyersLowsSpeed.html', {'form': buyersForm()})
	form_class = buyersForm
	template_name = 'buyersLowsSpeed.html'
	success_url = '/'
	success_message = "ثبت نام با موفقیت انجام شد"

class mtplusView(TemplateView):
	template_name='mtplus.html'



def ContactusView(request):
	
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']
			fullName = form.cleaned_data['fullName']
			recipients = ['farzan_salimiyan@yahoo.com']
			html_message = loader.render_to_string(
			'contactUsEmail.html',
			{
			'sender': sender,
			'subject': subject,
			'message': message,
			'fullName':fullName
			}
			)
			if cc_myself:
				recipients.append(sender)
			try:
				send_mail(subject, message, sender, recipients, html_message = html_message)
				return render(request, 'info.html', {'message': 'درخواست با موفقیت ارسال شد'})
			except:
				return render(request, 'Error.html', {'message': 'خطا در ارسال لطفا دوباره اقدام کنید'})
			return render(request, 'Error.html', {'message': 'خطا در ارسال لطفا دوباره اقدام کنید'})

	else:
		form = ContactForm()
		return render(request, 'contactUs.html', {'form': form})

