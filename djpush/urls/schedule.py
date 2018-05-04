from django.conf.urls import url
from djpush.views.schedule_api import ScheduleAPIView, ScheduleDeleteAPIView, ScheduleGetAPIView, ScheduleListAPIView

urlpatterns = [
    url(r'^$', ScheduleAPIView.as_view(), name='default'),
    url(r'^delete/?$', ScheduleDeleteAPIView.as_view(), name='delete'),
    url(r'^get/?$', ScheduleDeleteAPIView.as_view(), name='get'),
    url(r'^list/?$', ScheduleDeleteAPIView.as_view(), name='list'),
]
