import pandas
from django.core.management.base import BaseCommand

from game.models import Season, Week, Match
from team.models import Team


class Command(BaseCommand):
    def handle(self, *args, **options):
        season = None
        if not Season.objects.filter(year=2022).exists():
            season = Season.objects.create(year=2022)
            self.stdout.write(self.style.SUCCESS("Season were created"))

        if season:
            df = pandas.read_csv("./../season-22-23.csv")
            df.drop(
                [
                    "Day",
                    "Date",
                    "Time",
                    "TOL",
                    "YdsL",
                    "YdsW",
                    "TOW",
                    "PtsW",
                    "PtsL",
                    "Unnamed: 5",
                    "Unnamed: 7",
                ],
                inplace=True,
                axis=1,
            )

            for _, item in df.iterrows():
                week = Week.objects.get(name=f'Week {item["Week"]}')
                team = Team.objects.get(name=item["Winner/tie"])
                team2 = Team.objects.get(name=item["Loser/tie"])

                Match.objects.create(team1=team, team2=team2, week=week, season=season)

            self.stdout.write(self.style.SUCCESS("Matches were created"))
