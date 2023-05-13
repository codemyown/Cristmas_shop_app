# Generated by Django 4.1 on 2022-10-20 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("image", models.ImageField(upload_to="upload/images")),
                ("content", models.CharField(max_length=50)),
                ("desc", models.TextField()),
                ("date", models.CharField(max_length=40)),
            ],
        ),
    ]
