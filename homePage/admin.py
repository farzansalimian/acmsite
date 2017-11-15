from django.contrib import admin
from .models import news, aboutUs, introductionOfMembers, contests, UiaiFiles, UiaiimageArchiveList, contestsYearSemester, UiaiContext, acmContestsTeams, studentContests, studentContestsimageArchiveList, studentContestsFiles, studentContestsContext, uiai
# Register your models here.
admin.site.register(news)
admin.site.register(aboutUs)
admin.site.register(introductionOfMembers)
admin.site.register(UiaiFiles)
admin.site.register(UiaiimageArchiveList)
admin.site.register(contests)
admin.site.register(contestsYearSemester)
admin.site.register(acmContestsTeams)
admin.site.register(UiaiContext)
admin.site.register(studentContests)
admin.site.register(studentContestsContext)
admin.site.register(studentContestsFiles)
admin.site.register(studentContestsimageArchiveList)
admin.site.register(uiai)