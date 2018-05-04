from djpush.djpush import DJPushBasicClass


class DJPushReport(DJPushBasicClass):
    def message(self, msg_ids: str):
        return self.my_report.get_messages(msg_ids=msg_ids)

    def received(self, msg_ids: str):
        return self.my_report.get_received(msg_ids=msg_ids)

    def users(self, time_unit="DAY", start="2018-04-13", duration="3650"):
        return self.my_report.get_users(time_unit=time_unit, start=start, duration=duration)
