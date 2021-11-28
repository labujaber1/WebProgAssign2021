from django.forms import ModelForm
from .models import *
from django import forms

class customerRegisterForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class generalEnquiriesForm(ModelForm):
    class Meta:
        model=GeneralEnquiry
        fields='__all__'

class customerFittingForm(ModelForm):
    class Meta:
        model=BookFitting
        fields='__all__'    

class createorderform(ModelForm):
    class Meta:
        model=OrderForm
        fields="__all__"
        exclude=['orderStatus','quantity','stockCondition','summary','image','handycap'] 




