from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'pool',views.PollView)
#	url(r'^detail', views.PollView, name='detail'),
]


