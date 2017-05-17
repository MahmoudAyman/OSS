from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
url(r'^members/', include('members.urls')),
url(r'^gallery/', include('gallery.urls')),
url(r'^register/', include('register.urls')),
	url(r'^', include('landing.urls')),
    url(r'^admin/', admin.site.urls),
]
