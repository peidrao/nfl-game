from django.db import models
from user.models import Profile
from team.models import Team


class Season(models.Model):
    year = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)


class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='match_team1')
    team2 = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='match_team2')
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
