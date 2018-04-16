from rest_framework.response import Response
from rest_framework.views import APIView
from djpush.schedule import DJPushSchedule


class ScheduleDeleteAPIView(APIView, DJPushSchedule):
    def post(self):
        _data = self.request.DATA
        schedule_id = _data.get('schedule_id')
        res = self.delete_schedule(schedule_id=schedule_id)
        return Response(res)


class ScheduleGetAPIView(APIView, DJPushSchedule):
    def post(self):
        _data = self.request.DATA
        schedule_id = _data.get('schedule_id')
        res = self.get_schedule(schedule_id=schedule_id)
        return Response(res)


class ScheduleListAPIView(APIView, DJPushSchedule):
    def post(self):
        _data = self.request.DATA
        page = _data.get('page')
        res = self.get_schedule_list(page=page)
        return Response(res)


class ScheduleAPIView(APIView, DJPushSchedule)
    def post_schedule(self):
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="Hello, world!")
        push.platform = jpush.all_
        push = push.payload

        trigger = jpush.schedulepayload.trigger("2016-07-17 12:00:00")
        schedulepayload = jpush.schedulepayload.schedulepayload("name", True, trigger, push)
        return self.my_schedule.post_schedule(schedulepayload)

    def put_schedule(self):
        push = self.my_push
        push.audience = jpush.all_
        push.notification = jpush.notification(alert="Hello, world!")
        push.platform = jpush.all_
        push = push.payload
        trigger = jpush.schedulepayload.trigger("2016-05-17 12:00:00")
        schedulepayload = jpush.schedulepayload.schedulepayload("update a new name", True, trigger, push)
        return self.my_schedule.put_schedule(schedulepayload, "17349f00-0852-11e6-91b1-0021f653c902")
