from django.shortcuts import render
from django.views.generic import DetailView as DV
from django.views.generic.list import ListView as LV
from .models import news, aboutUs, introductionOfMembers, contests, UiaiimageArchiveList, UiaiFiles, contestsYearSemester, acmContestsTeams, UiaiContext, studentContests, studentContestsimageArchiveList, studentContestsFiles, studentContestsContext,uiai
from django.views.generic import CreateView as CV
from django.shortcuts import get_object_or_404
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
	models=contestsYearSemester
	template_name='contestsList.html'
	queryset=contestsYearSemester.objects.all()


class contentsFiles(LV):
	template_name ='contentsFiles.html'
	queryset=contests.objects.all()
	def get_context_data(self,**kwargs):
		context = super(contentsFiles,self).get_context_data(**kwargs)
		context['contests'] = contests.objects.filter(yearSemester__yearSemester=self.kwargs.get('yearSemester'))
		context['acmContestsTeams'] = acmContestsTeams.objects.filter(yearSemester__yearSemester=self.kwargs.get('yearSemester'))
		return context

class UiaiByYearSemester(LV):
	template_name ='uiaiByYearSemester.html'
	queryset = UiaiimageArchiveList.objects.all()
	def  get_context_data(self,**kwargs):
		context =super(UiaiByYearSemester,self).get_context_data(**kwargs)
		context['uiaiImage'] = UiaiimageArchiveList.objects.filter(yearSemester__yearSemester=self.kwargs.get('yearSemester'))
		context['uiaiFiles'] = UiaiFiles.objects.filter(yearSemester__yearSemester=self.kwargs.get('yearSemester'))
		context['UiaiContext'] = UiaiContext.objects.filter(yearSemester__yearSemester=self.kwargs.get('yearSemester'))
		return context

class uiaiList(LV):
	template_name='uiai.html'
	models=uiai
	queryset =uiai.objects.all()



class studentContestList(LV):
	template_name='studentsContest.html'
	models=studentContests
	queryset =studentContests.objects.all()

class studentContestByYearSemester(LV):
	template_name='studentsContestByYearSemester.html'
	queryset = studentContests.objects.all()
	def  get_context_data(self,**kwargs):
		context =super(studentContestByYearSemester,self).get_context_data(**kwargs)
		context['studentContestsImage'] = studentContestsimageArchiveList.objects.filter(yearSemester__yearSemester=self.kwargs.get('yearSemester'))
		context['studentContestsFiles'] = studentContestsFiles.objects.filter(yearSemester__yearSemester=self.kwargs.get('yearSemester'))
		context['studentContestsContext'] = studentContestsContext.objects.filter(yearSemester__yearSemester=self.kwargs.get('yearSemester'))
		return context