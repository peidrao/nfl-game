from django.db import models
from django.utils.translation import gettext_lazy as _

from app.domain.models.base import BaseModel


class Week(BaseModel):
    name = models.CharField(max_length=150, null=True)

    class Meta:
        verbose_name = _("week")
        verbose_name_plural = _("weeks")
        db_table = "db_week"
        ordering = ("id",)
