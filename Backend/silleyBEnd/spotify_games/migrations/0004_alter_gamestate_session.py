# Generated by Django 5.1.4 on 2025-02-10 20:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_games', '0003_alter_gamestate_current_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamestate',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamestate', to='spotify_games.gamesession'),
        ),
    ]
