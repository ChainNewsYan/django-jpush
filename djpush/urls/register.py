from django.conf.urls import url
from djpush.views.register import RegisterAPIView

urlpatterns = [
    url(r'^register/?$', RegisterAPIView.as_view(), name='register'),
]
