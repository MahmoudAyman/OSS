from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^form/$', views.form, name="form"),
    url(r'^login/$', views.logIn, name="login"),
    url(r'^signup/$', views.signUp, name="signup"),
    url(r'^logout/$', views.logOut, name="logout"),
]