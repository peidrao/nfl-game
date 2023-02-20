from django.core.management.base import BaseCommand

from user.models import Profile

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not Profile.objects.filter(email='admin@nfl.com').exists():
            profile = Profile.objects.create(email='admin@nfl.com', username='goat', first_name='Tom', last_name='GOAT Brady')
            profile.set_password('goat')
            profile.save()
            self.stdout.write(self.style.SUCCESS("Profile has created"))
