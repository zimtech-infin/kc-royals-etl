# Generated by Django 5.1.6 on 2025-02-23 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_remove_battingstat_caught_stealing_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='position',
            new_name='primary_position',
        ),
    ]
