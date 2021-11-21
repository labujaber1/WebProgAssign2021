from django.db import models
#from django.db.models.fields.related import ForeignKey


class Club(models.Model):
    CLUB_BRAND_CHOICES = (('WIL','Wilson'),('PK','Pike'),('FZ','Frazer'))
    CLUB_GRIPDIRECTION_CHOICES = (('LH','Left hand'),('RH','Right hand'))
    CLUB_TYPE_CHOICES = [
        ('OTHER', (
            ('DR','Driver'),('W','Wedge'),('P','Putter'),('F','Fairway')
            )
        ),
        ('IRON', (
            ('3i','3 iron'),('4i','4 iron'),('5i','5 iron'),('6i','6 iron'),
            ('7i','7 iron'),('8i','8 iron')
            )
        ),
        ]
    CLUB_GENDER_CHOICES= (('L','Ladies'),('M','Mens'),('J','Juniors'))
    CLUB_SIZE_CHOICES= (('SM','Short'),('M','Medium'),('L','Large'))
    STOCKCONDITION= (('OOS','Out of stock'),('IS','In stock'))
    club_image= models.ImageField(upload_to='images/', blank=True)
    club_name= models.CharField(max_length=20, blank=True)
    club_brand= models.CharField(max_length=20, choices=CLUB_BRAND_CHOICES, blank=True)
    club_type= models.CharField(max_length=20, choices=CLUB_TYPE_CHOICES, blank=True)
    club_summary= models.CharField(max_length=200, blank=True)
    club_size= models.CharField(max_length=10, choices=CLUB_SIZE_CHOICES, blank=True)
    club_gripDirection= models.CharField(max_length=10, choices=CLUB_GRIPDIRECTION_CHOICES, blank=True) 
    club_gender= models.CharField(max_length=10, choices=CLUB_GENDER_CHOICES, blank=True)
    club_price= models.DecimalField(max_digits=6, decimal_places=2)
    club_stockCondition= models.CharField(max_length=10, choices=STOCKCONDITION, default='IS')
    quantity= models.PositiveIntegerField(default=0)
    def _str_(self):
        return self.club_name

class SetOfClubs(models.Model):
    CLUB_SET_CHOICES= (('N','None'),('F','Full'),('H','Half'))
    STOCKCONDITION= (('OOS','Out of stock'),('IS','In stock'))
    CLUB_GENDER_CHOICES= (('L','Ladies'),('M','Mens'),('J','Juniors'))
    CLUB_SIZE_CHOICES= (('SM','Short'),('M','Medium'),('L','Large'))
    CLUB_BRAND_CHOICES = (('WIL','Wilson'),('PK','Pike'),('FZ','Frazer'))
    CLUB_GRIPDIRECTION_CHOICES = (('LH','Left hand'),('RH','Right hand'))
    clubSet_image= models.ImageField(upload_to='images/', blank=True)
    clubSet_type= models.CharField(max_length=10, choices=CLUB_SET_CHOICES, blank=True)
    clubSet_name= models.CharField(max_length=20, blank=True)
    clubSet_brand= models.CharField(max_length=20, choices=CLUB_BRAND_CHOICES, blank=True)
    clubSet_summary= models.CharField(max_length=200, blank=True)
    clubSet_size= models.CharField(max_length=10, choices=CLUB_SIZE_CHOICES, blank=True)
    clubSet_gripDirection= models.CharField(max_length=10, choices=CLUB_GRIPDIRECTION_CHOICES, blank=True) 
    clubSet_gender= models.CharField(max_length=10, choices=CLUB_GENDER_CHOICES, blank=True)
    clubSet_price= models.DecimalField(max_digits=6, decimal_places=2)
    clubSet_stockCondition= models.CharField(max_length=10, choices=STOCKCONDITION, default='IS')
    quantity= models.PositiveIntegerField(default=0)
    def _str_(self):
        return self.clubSet_name

class Accessories(models.Model):
    STOCKCONDITION= (('OOS','Out of stock'),('IS','In stock'))
    access_image= models.ImageField(upload_to='images/', blank=True)
    access_name = models.CharField(max_length=20, blank=True)
    access_description = models.CharField(max_length=30, blank=True)
    access_price = models.DecimalField(max_digits=5, decimal_places=2)
    access_stockCondition= models.CharField(max_length=10, choices=STOCKCONDITION, default='IS')
    quantity= models.PositiveIntegerField(default=0)
    def _str_(self):
        return self.access_name


class Customer(models.Model):
    GENDER_CHOICES= (('L','Lady'),('M','Male'),('J','Juniors'))
    first_name= models.CharField(max_length=20, blank=True)
    last_name= models.CharField(max_length=20, blank=True)
    gender= models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    def _str_(self):
        return self.last_name
        
class GeneralEnquiry(models.Model):
    name= models.CharField(max_length=30)
    email= models.CharField(max_length=30, blank=True)
    enquiry= models.CharField(max_length=300)
    phone_number= models.CharField(max_length=20, blank=True)
    def _str_(self):
        return self.name

class BookFitting(models.Model):
    name= models.CharField( max_length=30)
    customer_ID= models.CharField( max_length=10, blank=True)
    club_name= models.CharField( max_length=30)
    club_details= models.CharField( max_length=40, blank=True)
    fitting_date= models.CharField( max_length=30)
    contact_details= models.CharField(max_length=40)
    def _str_(self):
        return self.name

