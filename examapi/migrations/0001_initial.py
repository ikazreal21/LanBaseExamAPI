# Generated by Django 4.2 on 2023-04-07 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Questions",
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
                ("subject", models.CharField(max_length=250)),
                ("question", models.TextField()),
                ("mc1", models.CharField(max_length=255)),
                ("mc2", models.CharField(max_length=255)),
                ("mc3", models.CharField(max_length=255)),
                ("mc4", models.CharField(max_length=255)),
                ("mc5", models.CharField(max_length=255)),
                ("correct", models.CharField(max_length=15)),
            ],
        ),
    ]