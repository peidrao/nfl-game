from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from game.models import Match, Season
from team.models import Team


class Profile(AbstractUser):
    email = models.CharField(max_length=120, unique=True)

    about = models.TextField()
    has_team = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="images/profile/", null=True)
    is_start = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
        db_table = "db_profile"
        ordering = ("id",)


class TeamProfile(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("team of profile")
        verbose_name_plural = _("team of profiles")
        db_table = "db_team_profile"
        ordering = ("id",)


class SeasonProfile(models.Model):
    team = models.ForeignKey(TeamProfile, on_delete=models.SET_NULL, null=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("profile season")
        verbose_name_plural = _("profiles season")
        db_table = "db_season_profile"
        ordering = ("id",)


class GameWeek(models.Model):
    season = models.ForeignKey(SeasonProfile, on_delete=models.SET_NULL, null=True)
    match = models.ForeignKey(Match, on_delete=models.SET_NULL, null=True)
    scoreboard_home = models.IntegerField(default=0)
    scoreboard_away = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("game week")
        verbose_name_plural = _("games week")
        db_table = "db_game_week"
        ordering = ("id",)
