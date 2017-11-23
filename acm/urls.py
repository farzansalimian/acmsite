"""acm URL Configuration

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
from homePage.views import homepage , showDetailNews, aboutUsView, contestsList, uiaiList, contentsFiles, studentContestList, studentContestByYearSemester, UiaiByYearSemester
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage.as_view(),name='home'),
    url(r'^showDetailsNews/(?P<pk>\d+)/$', showDetailNews.as_view()),
    url(r'^aboutus/$', aboutUsView.as_view()),
    url(r'^contests/$', contestsList.as_view()),
    url(r'^uiai/(?P<yearSemester>.*)/$', UiaiByYearSemester.as_view()),
    url(r'^uiai/$', uiaiList.as_view()),
    url(r'^contests/(?P<yearSemester>.*)/$', contentsFiles.as_view()),
    url(r'^uispc/$', studentContestList.as_view()),
    url(r'^uispc/(?P<yearSemester>.*)/$', studentContestByYearSemester.as_view()),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
