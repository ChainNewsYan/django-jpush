import jpush
from jpush import common
from rest_framework.response import Response
from rest_framework.views import APIView

from djpush.djpush.zone import DJPushZone


class ZoneDefaultAPIView(APIView, DJPushZone):
    def post(self):
        _data = self.request.DATA
        alert = _data.get('alert')
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert=alert)
        push.platform = jpush.all_
        try:
            response = push.send()
        except common.Unauthorized:
            raise common.Unauthorized("Unauthorized")
        except common.APIConnectionException:
            raise common.APIConnectionException("conn")
        except common.JPushFailure:
            print("JPushFailure")
        except:
            print("Exception")
        return Response(response)


class ZoneBJAPIView(APIView, DJPushZone):

    def post(self):
        _data = self.request.DATA
        alert = _data.get('alert')
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert=alert)
        push.platform = jpush.all_
        try:
            response = push.send()
        except common.Unauthorized:
            raise common.Unauthorized("Unauthorized")
        except common.APIConnectionException:
            raise common.APIConnectionException("conn")
        except common.JPushFailure:
            print("JPushFailure")
        except:
            print("Exception")
        return Response(response)
