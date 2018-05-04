import jpush
from jpush import common

from djpush.djpush.basic import DJPushBasicClass


class DJPushZone(DJPushBasicClass):

    def default(self):
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="!hello python jpush api")
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

    def bj(self):
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="!hello python jpush api")
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
