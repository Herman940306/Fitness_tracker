# Generated by Django 5.1.3 on 2025-04-22 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("members", "0001_initial"),
        ("staff", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Visit",
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
                ("visit_date", models.DateTimeField()),
                ("purpose", models.CharField(max_length=255)),
                (
                    "staff",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="staff.staff",
                    ),
                ),
                (
                    "visitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="members.member"
                    ),
                ),
            ],
        ),
    ]
