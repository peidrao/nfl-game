# Generated by Django 4.1.7 on 2023-02-28 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("game", "0002_match_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Week",
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
                ("name", models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="match",
            name="week",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="game.week"
            ),
        ),
    ]