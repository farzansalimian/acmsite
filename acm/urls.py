"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin 
from showsomething.views import HomePage, ReviewS9, ReviewS9Plus, DetailsS9, DetailsS9Plus, ContactusView,  ReviewS9PlusLowSpeed, ReviewS9LowSpeed, BuyerViewLowSpeed, BuyerView ,mtplusView, DetailsS9LowSpeed, DetailsS9PlusLowSpeed, AskSpeed, lowSpeedView, MtpluslowSpeedView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/$', HomePage.as_view(), name='home'),
    url(r'^reviewS9plus/', ReviewS9Plus.as_view(), name='reviews9plus'),
    url(r'^reviewS9/', ReviewS9.as_view(), name='reviews9'),
    url(r'^reviewS9plusLowSpeed/', ReviewS9PlusLowSpeed.as_view(), name='reviews9plusLowSpeed'),
    url(r'^reviewS9LowSpeed/', ReviewS9LowSpeed.as_view(), name='reviews9LowSpeed'),
    url(r'^DetailsS9plus/', DetailsS9Plus.as_view(), name='Details9plus'),
    url(r'^DetailsS9/', DetailsS9.as_view(), name='Detailss9'),
    url(r'^buyS9/', BuyerView.as_view(), name='buyS9'),
    url(r'^buyS9LowSpeed/', BuyerViewLowSpeed.as_view(), name='buyS9LowSpeed'),
    url(r'^buyS9Plus/', BuyerView.as_view(), name='buyS9Plus'),
    url(r'^buyS9PlusLowSpeed/', BuyerViewLowSpeed.as_view(), name='buyS9PlusLowSpeed'),
    url(r'^mtplus/', mtplusView.as_view(), name='mtplus'),
    url(r'^$', AskSpeed.as_view(), name='askSpeed'),
    url(r'^lowSpeed/$', lowSpeedView.as_view(), name='lowSpeed'),
    url(r'^mtpluslowSpeed/$', MtpluslowSpeedView.as_view(), name='mtpluslowSpeed'),
    url(r'^DetailsS9pluslowSpeed/$', DetailsS9PlusLowSpeed.as_view(), name='Details9plusLowSpeed'),
    url(r'^DetailsS9lowSpeed/$', DetailsS9LowSpeed.as_view(), name='Detailss9LowSpeed'),
    url(r'^contactus/', ContactusView, name='contactusUrl'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

