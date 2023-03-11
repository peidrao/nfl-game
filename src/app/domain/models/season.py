from django.db import models
from django.utils.translation import gettext_lazy as _

from app.domain.models.base import BaseModel
from app.domain.models.profile import Profile
from app.domain.models.team import Team


class Season(BaseModel):
    year = models.IntegerField()

    class Meta:
        verbose_name = _("season")
        verbose_name_plural = _("seasons")
        db_table = "db_season"
        ordering = ("id",)


class SeasonProfile(BaseModel):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("profile season")
        verbose_name_plural = _("profiles season")
        db_table = "db_season_profile"
        ordering = ("id",)
