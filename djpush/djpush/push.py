import jpush

from djpush.djpush import DJPushBasicClass


class DjpushPush(DJPushBasicClass):
    def alias(self, alias: list, tags: list):
        push = self.my_push
        data = {'alias': alias}
        push.audience = jpush.audience(
            jpush.tag(*tags),
            data
        )
        push.notification = jpush.notification(alert="Hello world with audience!")
        push.platform = jpush.all_
        push.send()

    def all(self):
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
            print("JPushFailure")
        except:
            print("Exception")

    def audience(self, alias: list, tags: list):
        push = self.my_push

        push.audience = jpush.audience(
            jpush.tag(tags),
            jpush.alias(alias)
        )

        push.notification = jpush.notification(alert="Hello world with audience!")
        push.platform = jpush.all_
        push.send()

    def notification(self):
        push = self.my_push
        push.audience = jpush.all_
        push.platform = jpush.all_
        ios = jpush.ios(alert="Hello, IOS JPush!", sound="a.caf", extras={'k1': 'v1'})
        android = jpush.android(alert="Hello, Android msg", priority=1, style=1, alert_type=1, big_text='jjjjjjjjjj',
                                extras={'k1': 'v1'})
        push.notification = jpush.notification(alert="Hello, JPush!", android=android, ios=ios)
        push.send()

    def options(self):
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="Hello, world!")
        push.platform = jpush.all_
        push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": True}
        push.send()

    def platfrom_msg(self):
        push = self.my_push
        push.audience = jpush.all_
        ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", sound="a.caf", extras={'k1': 'v1'})
        android_msg = jpush.android(alert="Hello, android msg")
        push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
        push.message = jpush.message("content", extras={'k2': 'v2', 'k3': 'v3'})
        push.platform = jpush.all_
        push.send()

    def silent(self):
        push = self.my_push
        push.audience = jpush.all_
        ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", extras={'k1': 'v1'}, sound_disable=True)
        android_msg = jpush.android(alert="Hello, android msg")
        push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
        push.platform = jpush.all_
        push.send()

    def sms(self):
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="a sms message from python jpush api")
        push.platform = jpush.all_
        push.smsmessage = jpush.smsmessage("a sms message from python jpush api", 0)
        push.send()

    def validate(self):
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="Hello, world!")
        push.platform = jpush.all_
        push.send_validate()
