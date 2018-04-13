from django.conf.urls import url
from service.views.device_api import (
    AliasAPIView, )

urlpatterns = [
    url(r'^alias/?$', AliasAPIView.as_view(), name='alias'),
]
