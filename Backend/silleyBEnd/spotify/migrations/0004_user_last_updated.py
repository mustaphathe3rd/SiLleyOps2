# Generated by Django 5.1.4 on 2025-01-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0003_rename_duration_ms_mostlistenedsongs_duration_seconds_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
