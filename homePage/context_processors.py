from .models import news

def lastnews_processor(request):
	lastnews = news.objects.all()[:3]            
	return {'lastnews': lastnews}