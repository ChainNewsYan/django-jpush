"""django_jpush URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns

schema_view = get_schema_view(title='ChainNews API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^djpush/register/', include('djpush.urls.register', namespace='djpush-register')),
    url(r'^djpush/admin/', include('djpush.urls.admin', namespace='djpush-admin')),
    url(r'^djpush/device/', include('djpush.urls.device', namespace='djpush-device')),
    url(r'^djpush/push/', include('djpush.urls.push', namespace='djpush-push')),
    url(r'^djpush/schedule/', include('djpush.urls.schedule', namespace='djpush-schedule')),
    url(r'^djpush/zone/', include('djpush.urls.zone', namespace='djpush-zone')),
    url(r'^schema/$', schema_view),  # api docs
]

urlpatterns = format_suffix_patterns(urlpatterns)
