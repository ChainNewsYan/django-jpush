import jpush
import requests
from django.conf import settings
from requests import RequestException


class DJPushBasicClass(object):
    def __init__(self, fail_silently=False, *args, **kwargs):
        dev_key = kwargs.pop('dev_key', None)
        dev_secret = kwargs.pop('dev_secret', None)
        app_key = kwargs.pop('app_key', None)
        master_secret = kwargs.pop('master_secret', None)
        self.fail_silently = fail_silently
        try:
            self._dev_key = dev_key or getattr(settings, 'DEV_KEY')
            self._dev_secret = dev_secret or getattr(settings, 'DEV_SECRET')
            self._app_key = app_key or getattr(settings, 'APP_KEY')
            self._master_secret = master_secret or getattr(settings, 'MASTER_SECRET')
        except AttributeError:
            if self.fail_silently:
                self._dev_user = None
                self._dev_secret = None
                self._api_key = None
                self._master_secret = None
            else:
                raise

    @property
    def dev_key(self):
        return self._dev_key

    @property
    def dev_secret(self):
        return self._dev_secret

    @property
    def api_key(self):
        return self._app_key

    @property
    def master_secret(self):
        return self._master_secret

    @property
    def my_jpush(self):
        return jpush.JPush(key=self._app_key, secret=self._master_secret)

    @property
    def my_device(self):
        return self.my_jpush.create_device()

    @property
    def my_schedule(self):
        return self.my_jpush.create_schedule()

    @property
    def my_report(self):
        return self.my_jpush.create_report()

    @property
    def my_push(self):
        return self.my_jpush.create_push()

    def post_api(self, url, data):
        try:
            r = requests.post(url, data=data)
        except RequestException as e:
            if not self.fail_silently:
                raise e
            return False
        res = r.json()
        return res
