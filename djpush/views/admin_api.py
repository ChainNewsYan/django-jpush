from rest_framework.response import Response
from rest_framework.views import APIView

from djpush.djpush.admin import DJPushAdmin


class AdminAPIView(APIView):
    def get(self, request, *args, **kwargs):
        obj = DJPushAdmin()
        return Response(obj.admin)


class AdminCreateAPIView(APIView):
    def post(self):
        obj = DJPushAdmin()
        return Response(obj.create_app())


class AdminDeleteAPIView(APIView):
    def post(self):
        app_key = self.request.DATA.get('app_key')
        obj = DJPushAdmin()
        return Response(obj.delete_app(app_key))
