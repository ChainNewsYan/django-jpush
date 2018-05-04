from django.conf.urls import url
from djpush.views.device_api import (
    AliasAPIView, CtrlTagAPIView, DeviceAPIView, TagAPIView, TagCheckAPIView, UserTagAPIView, DeviceMobileUpdateAPIView)

urlpatterns = [
    url(r'^alias/?$', AliasAPIView.as_view(), name='alias'),
    url(r'^device/?$', DeviceAPIView.as_view(), name='device'),
    url(r'^device/mobile?$', DeviceMobileUpdateAPIView.as_view(), name='mobile'),
    url(r'^tag/?$', TagAPIView.as_view(), name='tag'),
    url(r'^tag/ctrl?$', CtrlTagAPIView.as_view(), name='ctrl'),
    url(r'^tag/check?$', TagCheckAPIView.as_view(), name='check'),
    url(r'^tag/user?$', UserTagAPIView.as_view(), name='user'),
]
