# Generated by Django 4.1.4 on 2023-05-22 14:36

import datetime
from django.db import migrations, models
import reservation.models


class Migration(migrations.Migration):

    dependencies = [
        (
            "reservation",
            "0008_alter_events_options_alter_calendarevent_end_time_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="calendarevent",
            name="end_time",
            field=reservation.models.CustomDateTimeField(
                default=datetime.datetime(2023, 5, 22, 15, 36, 9, 720281),
                help_text="Final time",
            ),
        ),
        migrations.AlterField(
            model_name="calendarevent",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime.now, help_text="Starting time"
            ),
        ),
    ]
