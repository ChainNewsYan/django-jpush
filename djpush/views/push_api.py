import jpush
from rest_framework.response import Response
from rest_framework.views import APIView

from djpush.djpush.basic import DJPushBasicClass


class AliasAPIView(DJPushBasicClass, APIView):
    def post(self, request):
        alias_list = self.request.data.get('alias_list', [])
        tags_list = self.request.data.get('tags_list', '')
        push = self.my_push
        push.audience = jpush.audience(
            jpush.tag(*tags_list),
            alias_list,
        )
        push.notification = jpush.notification(alert="Hello world with audience!")
        push.platform = jpush.all_
        res = push.send()
        return Response(res.payload)


class AllAPIView(DJPushBasicClass, APIView):
    def post(self, request):
        alert = self.request.data.get('alert', None)
        extras_data = self.request.data.get('extras', None)
        production = self.request.data.get('production', True)
        push = self.my_push
        push.audience = jpush.all_
        ios = jpush.ios(alert=alert, extras=extras_data, badge="+1")
        android = jpush.android(alert=alert, extras=extras_data)
        push.notification = jpush.notification(ios=ios, android=android)
        push.message = jpush.message("hi", extras=extras_data)
        push.platform = jpush.all_
        push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": production}
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
        return Response(response.payload)


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


class PlatformMsgAPIView(APIView, DJPushBasicClass):
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
