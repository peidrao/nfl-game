from django.core.management.base import BaseCommand

from game.models import Week


class Command(BaseCommand):
    def handle(self, *args, **options):
        for week in range(1, 19):
            Week.objects.create(name=f"Week {week}")

        self.stdout.write(self.style.SUCCESS("Weeks were created"))
