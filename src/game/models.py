from django.db import models
from team.models import Team


class Season(models.Model):
    year = models.IntegerField()
    is_active = models.BooleanField(default=True)


class Week(models.Model):
    name = models.CharField(max_length=150, null=True)


class Match(models.Model):
    team1 = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name="match_team1"
    )
    team2 = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name="match_team2"
    )
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    week = models.ForeignKey(Week, on_delete=models.SET_NULL, null=True)
