from django.db import models

# Create your models here.
class Club(models.Model):
    CLUB_BRAND_CHOICES = (('WIL','Wilson'),('PK','Pike'),('FZ','Frazer'))
    CLUB_GRIPDIRECTION_CHOICES = (('LH','Left hand'),('RH','Right hand'))
    CLUB_TYPE_CHOICES = [
        ('OTHER', (
            ('DR','Driver'),('W','Wedge'),('P','Putter')
            )
        ),
        ('IRON', (
            ('3i','3 iron'),('4i','4 iron'),('5i','5 iron'),('6i','6 iron'),
            ('7i','7 iron'),('8i','8 iron')
            )
        ),
        ('WOOD', (
            ('3w','3 wood'),('2w','2 wood'),('1w','1 wood')
            )
            ),
        ]
    CLUB_GENDER_CHOICES = (('L','Ladies'),('M','Mens'),('J','Juniors'))
    CLUB_SIZE_CHOICES = (('SM','Short'),('M','Medium'),('L','Large'))

    club_image = models.ImageField(upload_to='images/')
    club_name = models.CharField('Club name', max_length=50)
    club_brand = models.CharField(max_length=20, choices=CLUB_BRAND_CHOICES, blank=True)
    club_type = models.CharField(max_length=20, choices=CLUB_TYPE_CHOICES, blank=True)
    club_summary = models.CharField('Club summary',max_length=200)
    club_size = models.CharField(max_length=10, choices=CLUB_SIZE_CHOICES, blank=True)
    club_gripDirection = models.CharField(max_length=10, choices=CLUB_GRIPDIRECTION_CHOICES, blank=True) 
    club_gender = models.CharField(max_length=10, choices=CLUB_GENDER_CHOICES, blank=True)
    club_price = models.DecimalField(max_digits=5, decimal_places=2)
    def _str_(self):
        return self.club_name

class Club_set(models.Model):
    SET_BRAND_CHOICES = (('WIL','Wilson'),('PK','Pike'),('FZ','Frazer'))
    SET_GRIPDIRECTION_CHOICES = (('LH','Left hand'),('RH','Right hand'))
    SET_TYPE_CHOICES = (('F','Full'),('H','Half'))
    SET_GENDER_CHOICES = (('L','Ladies'),('M','Mens'),('J','Juniors'))
    SET_SIZE_CHOICES = (('SM','Short'),('M','Medium'),('L','Large'))

    set_image = models.ImageField(upload_to='images/')
    set_name = models.CharField('Set name',  max_length=50)
    set_brand = models.CharField(max_length=20, choices=SET_BRAND_CHOICES, blank=True)
    set_type = models.CharField(max_length=20, choices=SET_TYPE_CHOICES, blank=True)
    set_summary = models.CharField('Set summary',max_length=200)
    set_size = models.CharField(max_length=10, choices=SET_SIZE_CHOICES, blank=True)
    set_gripDirection = models.CharField(max_length=10, choices=SET_GRIPDIRECTION_CHOICES, blank=True) 
    set_gender = models.CharField(max_length=10, choices=SET_GENDER_CHOICES, blank=True)
    set_price = models.DecimalField(max_digits=5, decimal_places=2)

    def _str_(self):
        return self.set_name

class Customer(models.Model):
    CUSTOMER_GENDER_CHOICES = (('L','Ladies'),('M','Mens'),('J','Juniors'))
    CUSTOMER_TITLE_CHOICES = (('Mr','Mr'),('Mrs','Mrs'),('Miss','Miss'),('Ms','Ms'),('Mx','Mx'))
    customer_first_name = models.CharField(max_length=20)
    customer_last_name = models.CharField(max_length=20)
    customer_title = models.CharField(max_length=10, choices=CUSTOMER_TITLE_CHOICES, blank=True)
    customer_gender = models.CharField(max_length=20, choices=CUSTOMER_GENDER_CHOICES, blank=True)
    customer_email = models.CharField(max_length=20, blank=True)
    customer_phonenumber = models.CharField(max_length=20, blank=True)
    def _str_(self):
            return self.customer_last_name


