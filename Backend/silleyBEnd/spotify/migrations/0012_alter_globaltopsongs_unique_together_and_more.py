# Generated by Django 5.1.4 on 2025-01-10 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0011_remove_globaltopsongs_album_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='globaltopsongs',
            unique_together={('user', 'name', 'artists')},
        ),
        migrations.AlterUniqueTogether(
            name='topgenresongs',
            unique_together={('user', 'name', 'artists')},
        ),
    ]
