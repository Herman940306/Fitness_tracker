# Generated by Django 5.1.3 on 2025-04-22 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0001_initial"),
        ("visits", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="visit",
            name="visitor",
        ),
        migrations.AddField(
            model_name="visit",
            name="member",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="visits",
                to="members.member",
            ),
            preserve_default=False,
        ),
    ]
