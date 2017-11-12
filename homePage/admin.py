from django.contrib import admin
from .models import news, aboutUs, introductionOfMembers, imageArchive, contests
# Register your models here.
admin.site.register(news)
admin.site.register(aboutUs)
admin.site.register(introductionOfMembers)
admin.site.register(imageArchive)
