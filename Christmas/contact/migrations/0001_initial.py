# Generated by Django 4.1 on 2022-10-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("email", models.CharField(max_length=40)),
                ("phone", models.IntegerField(default=0)),
                ("message", models.TextField()),
            ],
        ),
    ]