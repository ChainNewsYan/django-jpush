import jpush
from rest_framework.response import Response
from rest_framework.views import APIView

from djpush.djpush.basic import DJPushBasicClass


class AliasAPIView(DJPushBasicClass, APIView):
    def get(self, request):
        alias = self.request.query_params.get('alias')
        platform = self.request.query_params.get('platform')
        res = self.my_device.get_aliasuser(alias=alias, platform=platform)
        return Response(res.payload)

    def delete(self, request):
        alias = self.request.data.get('alias', None)
        platform = self.request.data.get('platform', None)
        res = self.my_device.delete_alias(alias=alias, platform=platform)
        return Response(res.payload)


class CtrlTagAPIView(DJPushBasicClass, APIView):
    def post(self, request):
        reg_id = self.request.DATA.get('reg_id', None)
        tag = self.request.DATA.get('tag', None)
        entity = self.my_device.delete_tag(tag=tag)
        res = self.my_device.set_deviceinfo(registration_id=reg_id, entity=entity)
        return Response(res.payload)


class DeviceAPIView(DJPushBasicClass, APIView):
    def get(self, request):
        reg_id = self.request.query_params.get('reg_id', None)
        res = self.my_device.get_deviceinfo(registration_id=reg_id)
        return Response(res.payload)

    def post(self, request):
        tags = self.request.data.get('tags', None)
        reg_id = self.request.data.get('reg_id', None)
        # entity = jpush.my_device_tag(jpush.add("ddd", "tageee"))
        entity = jpush.device_tag(jpush.add(tags))
        res = self.my_device.set_devicemobile(registration_id=reg_id, entity=entity)
        return Response(res.payload)


class TagAPIView(DJPushBasicClass, APIView):
    def get(self, request):
        res = self.my_device.get_taglist()
        return Response(res.payload)

    def delete(self, request):
        tag = self.request.data.get('tag', None)
        platform = self.request.data.get('platform', None)
        res = self.my_device.delete_tag(tag=tag, platform=platform)
        return Response(res.payload)


class TagCheckAPIView(DJPushBasicClass, APIView):
    def get(self, request):
        tag = self.request.GET.get('tag')
        reg_id = self.request.GET.get('reg_id')
        res = self.my_device.check_taguserexist(tag=tag, registration_id=reg_id)
        return Response(res.payload)


class UserTagAPIView(DJPushBasicClass, APIView):
    def post(self, request):
        tag = self.request.data.get('tag')
        reg_id = self.request.data.get('reg_id')
        entity = jpush.device_regid(jpush.add(reg_id))
        res = self.my_device.update_tagusers(tag=tag, entity=entity)
        return Response(res.payload)


class DeviceMobileUpdateAPIView(DJPushBasicClass, APIView):
    def post(self, request):
        reg_id = self.request.data.get('reg_id')
        mobile = self.request.data.get('mobile')
        entity = jpush.device_mobile(mobile)
        res = self.my_device.set_devicemobile(registration_id=reg_id, entity=entity)
        return Response(res.payload)
