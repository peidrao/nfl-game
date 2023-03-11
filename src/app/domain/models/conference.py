from django.db import models
from django.utils.translation import gettext_lazy as _

from app.domain.models.base import BaseModel


class Conference(BaseModel):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=3)
    logo = models.CharField(max_length=250)

    class Meta:
        verbose_name = _("conferecy")
        verbose_name_plural = _("conferencies")
        db_table = "db_conferency"
        ordering = ("id",)
