from django.db import models


# Create your models here.
class ProductID(models.Model):
    SIZE_CHOICE = (('L','Ladies'),('M','Men'),('J','Junior'))
    GRIP_CHOICE = (('LH','Left Hand'),('RH','Right Hand'))
    CLUB_TYPE_CHOICE = [
        ('DR','Driver'),
        ('Woods', (
        ('3w','3 wood'),('2w','2 wood'),('1w','1 wood'),
        )),
        ('Iron', (
        ('3i','3 iron'),('4i','4 iron'),('5i','5 iron'),('6i','6 iron'),
        ('7i','7 iron'),('8i','8 iron'),
        )),
        ('W','Wedge'),
        ('P','Putter'),
    ]
    
    productName = models.CharField(max_length=100)
    productDescription = models.CharField(max_length=200, blank=True)
    productPrice = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.CharField(max_length=1, choices=SIZE_CHOICE, blank=True)
    grip = models.CharField(max_length=2, choices=GRIP_CHOICE, blank=True)
    clubType = models.CharField(max_length=2, choices=CLUB_TYPE_CHOICE, blank=True)
   
 
