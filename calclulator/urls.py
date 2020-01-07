from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$', views.top, name='top'),
    url(r'attacker', views.select_attacker, name='select_attacker'),
    url(r'attacked', views.select_attacked, name='select_attacked'),
    url(r'result', views.result, name='result'),
    url(r'policy', views.policy, name='policy')
]