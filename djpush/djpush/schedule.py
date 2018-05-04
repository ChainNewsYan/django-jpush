import jpush

from djpush.djpush.basic import DJPushBasicClass


class DJPushSchedule(DJPushBasicClass):
    def delete_schedule(self, schedule_id):
        return self.my_schedule.delete_schedule(schedule_id=schedule_id)

    def get_schedule(self, schedule_id):
        return self.my_schedule.delete_schedule(schedule_id=schedule_id)

    def get_schedule_list(self, page="1"):
        return self.my_schedule.get_schedule_list(page=page)

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
