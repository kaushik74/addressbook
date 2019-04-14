from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^contacts/', include('contacts.urls')),
    url('admin/', admin.site.urls),
]
