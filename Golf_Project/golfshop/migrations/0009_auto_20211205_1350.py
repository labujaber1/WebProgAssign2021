# Generated by Django 3.0.3 on 2021-12-05 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfshop', '0008_auto_20211201_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookfitting',
            old_name='club_name',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='bookfitting',
            name='club_details',
        ),
        migrations.RemoveField(
            model_name='bookfitting',
            name='customer_ID',
        ),
    ]
