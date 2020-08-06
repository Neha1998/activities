from django.core.management.base import BaseCommand
from user_activities.models import User, ActivityPeriod


class Command(BaseCommand):

    def _create_data(self):
        try:
            ap1 = ActivityPeriod(id=1, start_time="Feb 1 2020  1:33PM", end_time="Feb 1 2020 1:54PM")
            ap1.save()

            ap2 = ActivityPeriod(id=2, start_time="Mar 1 2020  11:11AM", end_time="Mar 1 2020 2:00PM")
            ap2.save()

            ap3 = ActivityPeriod(id=3, start_time="Mar 16 2020  5:33PM", end_time="Mar 16 2020 8:02PM")
            ap3.save()

            user = User(id=1, real_name='Egon Spengler', user_id="W012A3CDE", tz="America/Los_Angeles")
            user.save()
            user.activity_period.add(ap1, ap2, ap3)

            user = User(id=2, real_name='Glinda Southgood', user_id="W07QCRPA4", tz="Asia/Kolkata")
            user.save()
            user.activity_period.add(ap1, ap2)

        except Exception as err:
            print(err)

    def handle(self, *args, **options):
        self._create_data()
