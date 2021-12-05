from django.db import models
from django.db.models.deletion import SET_NULL
#from django.db.models.fields.related import ForeignKey


class Product(models.Model):
    BRAND_CHOICES = (('WIL','Wilson'),('PK','Pike'),('FZ','Frazer'))
    GRIPDIRECTION_CHOICES = (('LH','Left hand'),('RH','Right hand'))
    CLUB_TYPE_CHOICES = [
        ('OTHER', (
            ('F','FullSet'),('H','HalfSet'),
            ('DR','Driver'),('W','Wedge'),('P','Putter'),('F','Fairway')
            )
        ),
        ('IRON', (
            ('3i','3 iron'),('4i','4 iron'),('5i','5 iron'),('6i','6 iron'),
            ('7i','7 iron'),('8i','8 iron')
            )
        ),
        ]
    GENDER_CHOICES= (('L','Ladies'),('M','Mens'),('J','Juniors'))
    SIZE_CHOICES= (('SM','Short'),('M','Medium'),('L','Large'))
    STOCKCONDITION= (('OOS','Out of stock'),('IS','In stock'))
    CATEGORY_CHOICES= (('A','Accessory'),('C','Club'),('S','SetOfClubs'))
    image= models.ImageField(upload_to='images/', blank=True)
    name= models.CharField(max_length=20, blank=True)
    brand= models.CharField(max_length=20, choices=BRAND_CHOICES, blank=True)
    category= models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True)
    type= models.CharField(max_length=20, choices=CLUB_TYPE_CHOICES, blank=True)
    summary= models.CharField(max_length=200, blank=True)
    size= models.CharField(max_length=10, choices=SIZE_CHOICES, blank=True)
    gripDirection= models.CharField(max_length=10, choices=GRIPDIRECTION_CHOICES, blank=True) 
    gender= models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    stockCondition= models.CharField(max_length=10, choices=STOCKCONDITION, default='IS')
    quantity= models.PositiveIntegerField(default=0)
    def _str_(self):
        return self.club_name


class Customer(models.Model):
    GENDER_CHOICES= (('L','Lady'),('M','Male'),('J','Juniors'))
    first_name= models.CharField(max_length=20, blank=True)
    last_name= models.CharField(max_length=20, blank=True)
    gender= models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    handycap = models.PositiveIntegerField(default=0)
    email= models.CharField(max_length=30, blank=True)
    phone_number= models.CharField(max_length=20, blank=True)
    def _str_(self):
        return self.last_name
        
class GeneralEnquiry(models.Model):
    name= models.CharField(max_length=30)
    from_email= models.EmailField(max_length=30, blank=True)
    phone_number= models.CharField(max_length=20, blank=True)
    enquiry= models.TextField(max_length=300)
    def _str_(self):
        return self.name

class BookFitting(models.Model):
    name= models.CharField( max_length=30)
    customer_ID= models.CharField( max_length=10, blank=True)
    club_name= models.CharField( max_length=30)
    club_details= models.CharField( max_length=40, blank=True)
    fitting_date= models.DateField( max_length=30)
    contact_details= models.CharField(max_length=40)
    def _str_(self):
        return self.name

class OrderForm(models.Model):
    customer= models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL,)
    product= models.ForeignKey(Product, null=True, on_delete=SET_NULL,)
    orderDate = models.DateTimeField(auto_now_add=True)
    orderStatus = models.CharField(max_length=10, default='Unpaid')
   
    
    def _str_(self):
        return self.customer
