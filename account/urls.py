from django.conf.urls import include, url
from django.contrib import admin , auth
from django.urls import path
from . import views

urlpatterns = [
	#url(r'^login/$',views.user_login, name='login'),
	path('login/',views.user_login),
	path('', views.dashboard, name='dashboard'),

	path('login/',auth.login,name = 'login'),
	path('logout/',auth.logout,name = 'logout'),
	#path('logout-then-login/',views.logout-then-login,name = 'logout-then-login'),  

]


	# url(r'^login/$','django.contrib.auth.views.login',name = 'login'),
	# url(r'^logout/$','django.contrib.auth.views.logout',name = 'logout'),
	# url(r'^logout-then-login/$','django.contrib.auth.views.logout-then-login',name = 'logout-then-login'),  
