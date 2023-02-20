from re import L
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from team.models import Team



class Profile(AbstractUser):
    email = models.CharField(max_length=120, unique=True)

    about = models.TextField()
    has_team = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='images/profile/', null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
        db_table = 'db_profile'
        ordering = ('id',)



class TeamProfile(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('team of profile')
        verbose_name_plural = _('team of profiles')
        db_table = 'db_team_profile'
        ordering = ('id',)
