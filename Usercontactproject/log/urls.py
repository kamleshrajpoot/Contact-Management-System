#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^createcontact/$', views.createcontact, name='createcontact'),
    url(r'^update/(?P<pk>\d+)/$', views.update, name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='home'),



]
