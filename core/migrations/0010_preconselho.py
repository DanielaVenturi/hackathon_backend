# Generated by Django 5.1.2 on 2024-11-29 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_trimestre"),
    ]

    operations = [
        migrations.CreateModel(
            name="PreConselho",
            fields=[
                ("preConselho_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "trimestre",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.trimestre",
                    ),
                ),
                (
                    "turma",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.turma",
                    ),
                ),
            ],
        ),
    ]