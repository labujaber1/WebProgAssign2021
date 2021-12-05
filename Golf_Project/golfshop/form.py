from django.forms import ModelForm
from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#import floppyforms as forms


class customerRegisterForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class generalEnquiriesForm(ModelForm):
    class Meta:
        model=GeneralEnquiry
        fields='__all__'
   
class customerFittingForm(ModelForm):
    fitting_date = forms.DateField(widget = forms.SelectDateWidget)
    class Meta:
        model=BookFitting
        fields='__all__'    

class createorderform(ModelForm):
    order_date = forms.DateField(widget = forms.SelectDateWidget)
    class Meta:
        model=OrderForm
        fields="__all__"
        exclude=['orderStatus','quantity','stockCondition','summary','image','handycap'] 




