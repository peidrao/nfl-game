from django.db import models
from django.utils.translation import gettext_lazy as _

from app.domain.models.base import BaseModel
from app.domain.models.conference import Conference


class Division(BaseModel):
    name = models.CharField(max_length=20)
    conference = models.ForeignKey(
        Conference,
        on_delete=models.SET_NULL,
        null=True,
        related_name="division_conferency",
    )

    class Meta:
        verbose_name = _("division")
        verbose_name_plural = _("divisions")
        db_table = "db_division"
        ordering = ("id",)
