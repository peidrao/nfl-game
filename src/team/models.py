from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Conference(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=3)
    created_at = models.DateTimeField(default=timezone.now)
    logo = models.CharField(max_length=250)

    class Meta:
        verbose_name = _("conferecy")
        verbose_name_plural = _("conferencies")
        db_table = "db_conferency"
        ordering = ("id",)


class Division(models.Model):
    name = models.CharField(max_length=20)
    conference = models.ForeignKey(
        Conference,
        on_delete=models.SET_NULL,
        null=True,
        related_name="division_conferency",
    )

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _("division")
        verbose_name_plural = _("divisions")
        db_table = "db_division"
        ordering = ("id",)


class Team(models.Model):
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
