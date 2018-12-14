# pages/urls.py
from django.conf.urls import include, url
from .views import homePageView, index, cabinet, project, projects, catalog, signin

urlpatterns = [
    url(r'^cabinet/', cabinet, name='cabinet'),
    url(r'^catalog/', catalog.as_view(), name='catalog'),
    url(r'^project/test', project, name='project'),
    url(r'^signin/', signin.as_view(), name='signin'),
    url(r'^projects/', projects, name='projects'),
    url(r'^', index, name='home'),
]