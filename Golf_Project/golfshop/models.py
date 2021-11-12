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
    CLUB_SET_CHOICES = (('N','None'),('F','Full'),('H','Half'))
    CLUB_STOCKCONDITION = (('OOS','Out of stock'),('IS','In stock'))
    club_image = models.ImageField(upload_to='images/')
    club_name = models.CharField('Club name', max_length=50)
    club_brand = models.CharField(max_length=20, choices=CLUB_BRAND_CHOICES, blank=True)
    club_type = models.CharField(max_length=20, choices=CLUB_TYPE_CHOICES, blank=True)
    club_summary = models.CharField('Club summary',max_length=200)
    club_size = models.CharField(max_length=10, choices=CLUB_SIZE_CHOICES, blank=True)
    club_gripDirection = models.CharField(max_length=10, choices=CLUB_GRIPDIRECTION_CHOICES, blank=True) 
    club_gender = models.CharField(max_length=10, choices=CLUB_GENDER_CHOICES, blank=True)
    club_price = models.DecimalField(max_digits=5, decimal_places=2)
    club_set = models.CharField(max_length=10, choices=CLUB_SET_CHOICES, blank=True)
    club_quantity = models.PositiveIntegerField(default=0)
    club_stockCondition = models.CharField(max_length=10, choices=CLUB_STOCKCONDITION, default='IS')
    def _str_(self):
        return self.club_name

class Customer(models.Model):
    GENDER_CHOICES = (('L','Ladies'),('M','Mens'),('J','Juniors'))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES,blank=True)
    
    class Meta:
        verbose_name_plural = "Customer"
    def _str_(self):
            return self.last_name