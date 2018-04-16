import jpush
from rest_framework.response import Response
from rest_framework.views import APIView

from djpush.basic import DJPushBasicClass


class AlisaAPIView(APIView, DJPushBasicClass):
    def post(self):
        _data = self.request.DATA
        alias = _data.get('alias')
        tags = _data.get('tags')
        data = {'alisa': alias}
        push = self.my_push
        push.audience = jpush.audience(
            jpush.tag(*tags),
            data
        )
        push.notification = jpush.notification(alert="Hello world with audience!")
        push.platform = jpush.all_
        return Response(push.send())


class AllAPIView(APIView, DJPushBasicClass):
    def post(self):
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="!hello python jpush api")
        push.platform = jpush.all_
        try:
            response = push.send()
        except jpush.common.Unauthorized:
            raise jpush.common.Unauthorized("Unauthorized")
        except jpush.common.APIConnectionException:
            raise jpush.common.APIConnectionException("conn")
        except jpush.common.JPushFailure:
            raise ("JPushFailure",)
        except:
            raise ("Exception",)
        return Response(response)


class AudienceAPIView(APIView, DJPushBasicClass):
    def audience(self):
        _data = self.request.DATA
        alias = _data.get('alias')
        tags = _data.get('tags')
        push = self.my_push
        push.audience = jpush.audience(
            jpush.tag(tags),
            jpush.alias(alias)
        )
        push.notification = jpush.notification(alert="Hello world with audience!")
        push.platform = jpush.all_
        return Response(push.send())


class NotificationAPIView(APIView, DJPushBasicClass):
    def post(self):
        push = self.my_push
        push.audience = jpush.all_
        push.platform = jpush.all_
        ios = jpush.ios(alert="Hello, IOS JPush!", sound="a.caf", extras={'k1': 'v1'})
        android = jpush.android(alert="Hello, Android msg", priority=1, style=1, alert_type=1, big_text='jjjjjjjjjj',
                                extras={'k1': 'v1'})
        push.notification = jpush.notification(alert="Hello, JPush!", android=android, ios=ios)
        push.send()


class OptionsAPIView(APIView, DJPushBasicClass):
    def post(self):
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="Hello, world!")
        push.platform = jpush.all_
        push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": True}
        return Response(push.send())


class PlatformMsg(APIView, DJPushBasicClass):
    def post(self):
        push = self.my_push
        push.audience = jpush.all_
        ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", sound="a.caf", extras={'k1': 'v1'})
        android_msg = jpush.android(alert="Hello, android msg")
        push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
        push.message = jpush.message("content", extras={'k2': 'v2', 'k3': 'v3'})
        push.platform = jpush.all_
        return Response(push.send())


class SilentAPIView(APIView, DJPushBasicClass):
    def post(self):
        push = self.my_push
        push.audience = jpush.all_
        ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", extras={'k1': 'v1'}, sound_disable=True)
        android_msg = jpush.android(alert="Hello, android msg")
        push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
        push.platform = jpush.all_
        return Response(push.send())


class SmsAPIView(APIView, DJPushBasicClass):
    def post(self):
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="a sms message from python jpush api")
        push.platform = jpush.all_
        push.smsmessage = jpush.smsmessage("a sms message from python jpush api", 0)
        return Response(push.send())


class ValidateAPIView(APIView, DJPushBasicClass):
    def post(self):
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="Hello, world!")
        push.platform = jpush.all_
        return Response(push.send_validate())
