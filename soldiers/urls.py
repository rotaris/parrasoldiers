"""parrasoldiers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from soldiers import views

urlpatterns = [
    url(r'^all', views.all_soldiers, name='home'),
    url(r'^list_all_soldiers$', views.list_all_soldiers, name='list_all_soldiers'),
    url(r'^(?P<unique_id>[0-9]+)/records/', views.soldier_records, name='soldier_records'),
    url(r'^(?P<unique_id>[0-9]+)', views.soldier_detail, name='soldier_detail'),
]
