from django.conf.urls import url
from djpush.views.admin_api import AdminAPIView, AdminCreateAPIView, AdminDeleteAPIView

urlpatterns = [
    # url(r'^$', AdminAPIView.as_view(), name='list'),
    url(r'^create/?$', AdminCreateAPIView.as_view(), name='create'),
    url(r'^delete/?$', AdminDeleteAPIView.as_view(), name='delete'),
]
