# Generated by Django 4.1.7 on 2023-02-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ResultType1",
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
                ("d1", models.FloatField()),
                ("d2", models.FloatField()),
                ("d3", models.FloatField()),
            ],
        ),
    ]
