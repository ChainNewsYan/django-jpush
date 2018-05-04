import jpush

from djpush.djpush.basic import DJPushBasicClass


class DJPushAdmin(DJPushBasicClass):
    def __init__(self, *args, **kwargs):
        self.app_name = kwargs.pop('app_name', None)
        self.android_package = kwargs.pop('android_package', None)
        self.group_name = kwargs.pop('group_name', None)
        super(DJPushAdmin, self).__init__(*args, **kwargs)

    @property
    def admin(self):
        return jpush.Admin(key=self.dev_key, secret=self.dev_secret)

    def create_app(self):
        return self.admin.create_app(app_name=self.app_name,
                                     android_package=self.android_package,
                                     group_name=self.group_name)

    def delete_app(self, app_key):
        return self.admin.delete_app(app_key)
