from django.conf.urls import url
from djpush.views.push_api import (AudienceAPIView, AllAPIView, NotificationAPIView, OptionsAPIView,
                                    SilentAPIView, SmsAPIView, PlatformMsgAPIView, ValidateAPIView, AliasAPIView)

urlpatterns = [
    url(r'^alias/?$', AliasAPIView.as_view(), name='alias'),
    url(r'^audience/?$', AudienceAPIView.as_view(), name='audience'),
    url(r'^all/?$', AllAPIView.as_view(), name='all'),
    url(r'^notification/?$', NotificationAPIView.as_view(), name='notification'),
    url(r'^options/?$', OptionsAPIView.as_view(), name='options'),
    url(r'^silent/?$', SilentAPIView.as_view(), name='silent'),
    url(r'^sms/?$', SmsAPIView.as_view(), name='sms'),
    url(r'^platform/?$', PlatformMsgAPIView.as_view(), name='platform'),
    url(r'^validate/?$', ValidateAPIView.as_view(), name='validate'),
]
