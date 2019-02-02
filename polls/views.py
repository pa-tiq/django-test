from django.http import HttpResponse

def index(request):
	return HttpResponse("yee \n polls index")