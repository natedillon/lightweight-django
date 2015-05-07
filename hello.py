from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse


# View
def index(request):
	return HttpResponse('Hello World')


# URLs
urlpatterns = (
	url(r'^$', index)
)


# Settings
settings.configure(
	DEBUG = True,
	SECRET_KEY = 'thisisthesecretkey',
	ROOT_URLCONF = __name__,
	MIDDLEWARE_CLASSES = (
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.middleware.clickjacking.XFrameOptionsMiddleware',
	),
)
