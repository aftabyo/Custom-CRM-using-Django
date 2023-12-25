# management/commands/check_meetups.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from website.models import Record

class Command(BaseCommand):
    help = 'Check upcoming meetups and set notification_sent'

    def handle(self, *args, **options):
        upcoming_meetups = Record.objects.filter(
            meetup__gt=timezone.now(),
            meetup__lte=timezone.now() + timezone.timedelta(days=2),
            notification_sent=False,
        )

        for meetup in upcoming_meetups:
            days_until_meetup = (meetup.meetup - timezone.now().date()).days

            if days_until_meetup == 2:
                meetup.notification_sent = True
                meetup.save()
            elif days_until_meetup == 1:
                meetup.notification_sent = True
                meetup.save()
            elif days_until_meetup == 0:
                meetup.notification_sent = True
                meetup.save()
