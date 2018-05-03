from django.conf.urls import url
from service.views.register import RegisterAPIView

urlpatterns = [
    url(r'^register/?$', RegisterAPIView.as_view(), name='register'),
]
