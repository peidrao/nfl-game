import pandas
from django.core.management.base import BaseCommand

from app.domain.models.season import Season
from app.domain.models.week import Week
from app.domain.models.match import Match
from app.domain.models.team import Team


class Command(BaseCommand):
    def handle(self, *args, **options):
        season = None
        if not Season.objects.filter(year=2022).exists():
            season = Season.objects.create(year=2022)
            self.stdout.write(self.style.SUCCESS("Season were created"))

        if season:
            df = pandas.read_csv("./../fake_season.csv")
            df.drop(
                [
                    "game_type",
                    "away_rest",
                    "home_rest",
                    "location",
                    "result",
                ],
                inplace=True,
                axis=1,
            )

            for _, item in df.iterrows():
                week = Week.objects.get(name=f'Week {item["week"]}')
                home = Team.objects.get(abbreviation=item["home_team"])
                away = Team.objects.get(abbreviation=item["away_team"])

                Match.objects.create(away=away, home=home, week=week, season=season)

            self.stdout.write(self.style.SUCCESS("Matches were created"))
