from django.db import models
from django.utils.translation import gettext_lazy as _

from app.domain.models.base import BaseModel
from app.domain.models.season import Season, SeasonProfile
from app.domain.models.team import Team
from app.domain.models.week import Week


class Match(BaseModel):
    home = models.ForeignKey(
        Team(), on_delete=models.SET_NULL, null=True, related_name="home_team"
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


class GameMatchWeek(BaseModel):
    season = models.ForeignKey(SeasonProfile, on_delete=models.SET_NULL, null=True)
    match = models.ForeignKey(Match, on_delete=models.SET_NULL, null=True)
    scoreboard_home = models.IntegerField(default=0)
    scoreboard_away = models.IntegerField(default=0)
    is_closed = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("game week")
        verbose_name_plural = _("games week")
        db_table = "db_game_week"
        ordering = ("id",)
