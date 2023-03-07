from django.db import models
from team.models import Team
from django.utils.translation import gettext_lazy as _


class Season(models.Model):
    year = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("season")
        verbose_name_plural = _("seasons")
        db_table = "db_season"
        ordering = ("id",)


class Week(models.Model):
    name = models.CharField(max_length=150, null=True)

    class Meta:
        verbose_name = _("week")
        verbose_name_plural = _("weeks")
        db_table = "db_week"
        ordering = ("id",)


class Match(models.Model):
    home = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name="home_team"
    )
    away = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name="away_team"
    )
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    week = models.ForeignKey(Week, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("match")
        verbose_name_plural = _("matches")
        db_table = "db_match"
        ordering = ("id",)
