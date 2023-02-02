# Generated by Django 4.1.4 on 2023-01-18 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orm1", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=40)),
            ],
            options={"db_table": "Country",},
        ),
        migrations.CreateModel(
            name="Capital",
            fields=[
                (
                    "country",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="orm1.country",
                    ),
                ),
                ("name", models.CharField(max_length=34)),
            ],
            options={"db_table": "Capital",},
        ),
    ]
