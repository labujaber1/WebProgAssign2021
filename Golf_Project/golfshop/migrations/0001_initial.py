# Generated by Django 3.0.3 on 2021-11-12 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookFitting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('customer_ID', models.CharField(blank=True, max_length=10, verbose_name='CustomerId')),
                ('clubName', models.CharField(max_length=30, verbose_name='clubName')),
                ('clubDetails', models.CharField(blank=True, max_length=40, verbose_name='clubDetails')),
                ('fittingDate', models.CharField(max_length=30, verbose_name='FitDate')),
                ('contactDetails', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_image', models.ImageField(upload_to='images/')),
                ('club_name', models.CharField(max_length=50, verbose_name='Club name')),
                ('club_brand', models.CharField(blank=True, choices=[('WIL', 'Wilson'), ('PK', 'Pike'), ('FZ', 'Frazer')], max_length=20)),
                ('club_type', models.CharField(blank=True, choices=[('OTHER', (('DR', 'Driver'), ('W', 'Wedge'), ('P', 'Putter'))), ('IRON', (('3i', '3 iron'), ('4i', '4 iron'), ('5i', '5 iron'), ('6i', '6 iron'), ('7i', '7 iron'), ('8i', '8 iron'))), ('WOOD', (('3w', '3 wood'), ('2w', '2 wood'), ('1w', '1 wood')))], max_length=20)),
                ('club_summary', models.CharField(max_length=200, verbose_name='Club summary')),
                ('club_size', models.CharField(blank=True, choices=[('SM', 'Short'), ('M', 'Medium'), ('L', 'Large')], max_length=10)),
                ('club_gripDirection', models.CharField(blank=True, choices=[('LH', 'Left hand'), ('RH', 'Right hand')], max_length=10)),
                ('club_gender', models.CharField(blank=True, choices=[('L', 'Ladies'), ('M', 'Mens'), ('J', 'Juniors')], max_length=10)),
                ('club_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('club_set', models.CharField(blank=True, choices=[('N', 'None'), ('F', 'Full'), ('H', 'Half')], max_length=10)),
                ('club_quantity', models.PositiveIntegerField(default=0)),
                ('club_stockCondition', models.CharField(choices=[('OOS', 'Out of stock'), ('IS', 'In stock')], default='IS', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=20)),
                ('lname', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('L', 'Ladies'), ('M', 'Mens'), ('J', 'Juniors')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('email', models.CharField(blank=True, max_length=30, verbose_name='email')),
                ('enquiry', models.CharField(max_length=300, verbose_name='enquiry')),
                ('phoneNumber', models.CharField(blank=True, max_length=20, verbose_name='phone')),
            ],
        ),
    ]
