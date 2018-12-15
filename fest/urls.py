# pages/urls.py
from django.conf.urls import include, url
from .views import homePageView, index, cabinet, project, projects, catalog, signin, about
from .views import reg_org

urlpatterns = [
    url(r'^cabinet/', cabinet, name='cabinet'),
    url(r'^catalog/', catalog, name='catalog'),
    url(r'^project/test', project, name='project'),
    url(r'^signin/', signin, name='signin'),
    url(r'^projects/', projects, name='projects'),
    url(r'^about/', about, name='about'),
    url(r'^reg_org/', reg_org, name='reg_org'),
    url(r'^', index, name='home'),
]