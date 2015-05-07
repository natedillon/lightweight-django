from django.conf.urls import url
from django.http import HttpResponse


# View
def index(request):
	return HttpResponse('Hello World')


# URLs
urlpatterns = (
	url(r'^$', index)
)
