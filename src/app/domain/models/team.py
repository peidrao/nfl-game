from django.db import models
from django.utils.translation import gettext_lazy as _

from app.domain.models.base import BaseModel
from app.domain.models.division import Division


class Team(BaseModel):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=4)
    stadium = models.CharField(max_length=100)
    division = models.ForeignKey(
        Division, on_delete=models.SET_NULL, null=True, related_name="team_division"
    )
    logo = models.CharField(max_length=250)

    primary_color = models.CharField(max_length=20)
    secondary_color = models.CharField(max_length=20)

    class Meta:
        verbose_name = _("team")
        verbose_name_plural = _("teams")
        db_table = "db_team"
        ordering = ("id",)
