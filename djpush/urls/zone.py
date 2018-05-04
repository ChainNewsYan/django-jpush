from django.conf.urls import url
from djpush.views.zone_api import ZoneDefaultAPIView, ZoneBJAPIView

urlpatterns = [
    url(r'^default/?$', ZoneDefaultAPIView.as_view(), name='default'),
    url(r'^bj/?$', ZoneBJAPIView.as_view(), name='bj'),
]
