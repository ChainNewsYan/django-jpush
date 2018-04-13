import jpush
from rest_framework.response import Response
from rest_framework.views import APIView

from djpush.basic import DJPushBasicClass


class AliasAPIView(APIView, DJPushBasicClass):
    def get(self):
        alias = self.request.query_params.get('alias', None)
        platform = self.request.query_params.get('platform', None)
        res = self.my_device.get_aliasuser(alias=alias, platform=platform)
        return Response(res.payload)

    def delete(self):
        alias = self.request.quert.get('alias', None)
        platform = self.request.GET.get('platform', None)
        res = self.my_device.delete_alias(alias=alias, platform=platform)
        return Response(res.payload)


class CtrlTagAPIView(APIView, DJPushBasicClass):
    def post(self):
        reg_id = self.request.DATA.get('reg_id', None)
        tag = self.request.DATA.get('tag', None)
        entity = self.my_device.delete_tag(tag=tag)
        res = self.my_device.set_deviceinfo(registration_id=reg_id, entity=entity)
        return Response(res.payload)


class DeviceAPIView(APIView, DJPushBasicClass):
    def get(self):
        reg_id = self.request.query_params.get('reg_id', None)
        res = self.my_device.get_deviceinfo(registration_id=reg_id)
        return Response(res.payload)

    def put(self):
        tags = self.request.DATA.get('tags', None)
        reg_id = self.request.DATA.get('reg_id', None)
        # entity = jpush.my_device_tag(jpush.add("ddd", "tageee"))
        entity = jpush.device_tag(jpush.add(tags))
        res = self.my_device.set_devicemobile(registration_id=reg_id, entity=entity)
        return Response(res.payload)


class TagAPIView(APIView, DJPushBasicClass):
    def get(self):
        res = self.my_device.get_taglist()
        return Response(res.payload)

    def delete(self):
        tag = self.request.query_params.get('tag', None)
        platform = self.request.query_params.get('platform', None)
        res = self.my_device.delete_tag(tag=tag, platform=platform)
        return Response(res.payload)


class TagCheckAPIView(APIView, DJPushBasicClass):
    def get(self):
        tag = self.request.GET.get('tag')
        reg_id = self.request.GET.get('reg_id')
        res = self.my_device.check_taguserexist(tag=tag, registration_id=reg_id)
        return Response(res.payload)


class UserTagAPIView(APIView, DJPushBasicClass):
    def put(self):
        tag = self.request.DATA.get('tag')
        reg_id = self.request.DATA.get('reg_id')
        entity = jpush.device_regid(jpush.add(reg_id))
        res = self.my_device.update_tagusers(tag=tag, entity=entity)
        return Response(res.payload)


class DeviceMobileUpdateAPIView(APIView, DJPushBasicClass):
    def put(self):
        reg_id = self.request.query_params.get('reg_id')
        mobile = self.request.query_params.get('mobile')
        entity = jpush.device_mobile(mobile)
        res = self.my_device.set_devicemobile(registration_id=reg_id, entity=entity)
        return Response(res.payload)