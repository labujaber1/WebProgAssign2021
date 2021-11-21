# Generated by Django 3.0.3 on 2021-11-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_image', models.ImageField(blank=True, upload_to='images/')),
                ('access_name', models.CharField(blank=True, max_length=20)),
                ('access_description', models.CharField(blank=True, max_length=30)),
                ('access_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('access_stockCondition', models.CharField(choices=[('OOS', 'Out of stock'), ('IS', 'In stock')], default='IS', max_length=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BookFitting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('customer_ID', models.CharField(blank=True, max_length=10)),
                ('club_name', models.CharField(max_length=30)),
                ('club_details', models.CharField(blank=True, max_length=40)),
                ('fitting_date', models.CharField(max_length=30)),
                ('contact_details', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_image', models.ImageField(blank=True, upload_to='images/')),
                ('club_name', models.CharField(blank=True, max_length=20)),
                ('club_brand', models.CharField(blank=True, choices=[('WIL', 'Wilson'), ('PK', 'Pike'), ('FZ', 'Frazer')], max_length=20)),
                ('club_type', models.CharField(blank=True, choices=[('OTHER', (('DR', 'Driver'), ('W', 'Wedge'), ('P', 'Putter'), ('F', 'Fairway'))), ('IRON', (('3i', '3 iron'), ('4i', '4 iron'), ('5i', '5 iron'), ('6i', '6 iron'), ('7i', '7 iron'), ('8i', '8 iron')))], max_length=20)),
                ('club_summary', models.CharField(blank=True, max_length=200)),
                ('club_size', models.CharField(blank=True, choices=[('SM', 'Short'), ('M', 'Medium'), ('L', 'Large')], max_length=10)),
                ('club_gripDirection', models.CharField(blank=True, choices=[('LH', 'Left hand'), ('RH', 'Right hand')], max_length=10)),
                ('club_gender', models.CharField(blank=True, choices=[('L', 'Ladies'), ('M', 'Mens'), ('J', 'Juniors')], max_length=10)),
                ('club_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('club_stockCondition', models.CharField(choices=[('OOS', 'Out of stock'), ('IS', 'In stock')], default='IS', max_length=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('L', 'Lady'), ('M', 'Male'), ('J', 'Juniors')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('enquiry', models.CharField(max_length=300)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SetOfClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clubSet_image', models.ImageField(blank=True, upload_to='images/')),
                ('clubSet_type', models.CharField(blank=True, choices=[('N', 'None'), ('F', 'Full'), ('H', 'Half')], max_length=10)),
                ('clubSet_name', models.CharField(blank=True, max_length=20)),
                ('clubSet_brand', models.CharField(blank=True, choices=[('WIL', 'Wilson'), ('PK', 'Pike'), ('FZ', 'Frazer')], max_length=20)),
                ('clubSet_summary', models.CharField(blank=True, max_length=200)),
                ('clubSet_size', models.CharField(blank=True, choices=[('SM', 'Short'), ('M', 'Medium'), ('L', 'Large')], max_length=10)),
                ('clubSet_gripDirection', models.CharField(blank=True, choices=[('LH', 'Left hand'), ('RH', 'Right hand')], max_length=10)),
                ('clubSet_gender', models.CharField(blank=True, choices=[('L', 'Ladies'), ('M', 'Mens'), ('J', 'Juniors')], max_length=10)),
                ('clubSet_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('clubSet_stockCondition', models.CharField(choices=[('OOS', 'Out of stock'), ('IS', 'In stock')], default='IS', max_length=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
