# Generated by Django 4.1.7 on 2023-03-06 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("game", "0002_remove_match_team1_remove_match_team2_match_away_and_more"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SeasonProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "season",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="game.season",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="user.teamprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GameWeek",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("scoreboard_home", models.IntegerField(default=0)),
                ("scoreboard_away", models.IntegerField(default=0)),
                (
                    "match",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="game.match",
                    ),
                ),
                (
                    "season",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="user.seasonprofile",
                    ),
                ),
            ],
        ),
    ]
