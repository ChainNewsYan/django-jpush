import jpush
from rest_framework.response import Response
from rest_framework.views import APIView
from djpush.djpush.schedule import DJPushSchedule


class ScheduleDeleteAPIView(APIView, DJPushSchedule):
    def post(self):
        _data = self.request.DATA
        schedule_id = _data.get('schedule_id')
        res = self.delete_schedule(schedule_id=schedule_id)
        return Response(res)


class ScheduleGetAPIView(APIView, DJPushSchedule):
    def get(self):
        _data = self.request.query_params
        schedule_id = _data.get('schedule_id')
        res = self.get_schedule(schedule_id=schedule_id)
        return Response(res)


class ScheduleListAPIView(APIView, DJPushSchedule):
    def post(self):
        _data = self.request.DATA
        page = _data.get('page')
        res = self.get_schedule_list(page=page)
        return Response(res)


class ScheduleAPIView(APIView, DJPushSchedule):
    def post(self):
        _data = self.request.DATA
        alert = _data.get('alert')
        time = _data.get('time')  # "2016-07-17 12:00:00"
        name = _data.get('name')
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert=alert)
        push.platform = jpush.all_
        push = push.payload
        trigger = jpush.schedulepayload.trigger(time)
        schedulepayload = jpush.schedulepayload.schedulepayload(name, True, trigger, push)
        return self.my_schedule.post_schedule(schedulepayload)

    def put(self):
        _data = self.request.DATA
        alert = _data.get('alert')  # "Hello, world!"
        time = _data.get('time')  # "2016-07-17 12:00:00"
        name = _data.get('name')
        schedule_id = _data.get('schedule_id')  # "17349f00-0852-11e6-91b1-0021f653c902"
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert=alert)
        push.platform = jpush.all_
        push = push.payload
        trigger = jpush.schedulepayload.trigger(time)
        schedulepayload = jpush.schedulepayload.schedulepayload(name, True, trigger, push)
        return self.my_schedule.put_schedule(schedulepayload, schedule_id)
