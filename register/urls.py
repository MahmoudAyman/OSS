from django.conf.urls import url, include
from . import views

app_name = "register"

urlpatterns = [
    url(r'^$', views.form, name="form"),
    url(r'^/login/$', views.logIn, name="login"),
    url(r'^/signup/$', views.signUp, name="signup"),
    url(r'^/logout/$', views.logOut, name="logout"),
]