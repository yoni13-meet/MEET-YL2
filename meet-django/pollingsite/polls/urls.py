from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	url(r'pizza/$', views.pizza, name="pizza"),

	url(r'burger/$', views.burger, name="burger"),
	url(r'hotdog/$', views.hotdog, name="hotdog"),
)
