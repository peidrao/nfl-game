import json

from django.core.management.base import BaseCommand

from team.models import Conference, Division, Team


CONFERENCES = [
    {"name": "National Football Conference", "abbreviation": "NFC", "logo": "nfc.png"},
    {"name": "American Football Conference", "abbreviation": "AFC", "logo": "afc.png"},
]
DIVISIONS = ["North", "South", "East", "West"]


class Command(BaseCommand):
    def handle(self, *args, **options):
        conferences = []

        if not Conference.objects.all().count() == 2:
            for conf in CONFERENCES:
                c = Conference.objects.create(**conf)
                conferences.append(c)
            self.stdout.write(self.style.SUCCESS("Conferences were created"))

        if not Division.objects.all().count() == 8:
            for divi in DIVISIONS:
                Division.objects.bulk_create(
                    [
                        Division(name=divi, conference=conferences[0]),
                        Division(name=divi, conference=conferences[1]),
                    ]
                )

            self.stdout.write(self.style.SUCCESS("Divisions were created"))
        file = open("../teams.json")
        teams = json.load(file)

        for team in teams:
            if not Team.objects.filter(name=team["name"]).exists():
                division = Division.objects.get(
                    name=team["division"], conferency__abbreviation=team["tag"]
                )
                Team.objects.create(
                    name=team["name"],
                    stadium=team["stadium"],
                    logo=team["logo"],
                    primary_color=team["primary_color"],
                    secondary_color=team["secondary_color"],
                    division=division,
                )
        self.stdout.write(self.style.SUCCESS("Teams were created"))
