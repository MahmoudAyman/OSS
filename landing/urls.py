from django.conf.urls import url, include

from . import views

app_name = "landing"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^collaborators/', include('members.urls')),
]