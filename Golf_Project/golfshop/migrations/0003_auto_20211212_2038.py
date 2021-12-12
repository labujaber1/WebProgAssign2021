# Generated by Django 3.0.3 on 2021-12-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfshop', '0002_auto_20211212_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderrequest',
            old_name='product',
            new_name='productName',
        ),
        migrations.AddField(
            model_name='orderrequest',
            name='productID',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
