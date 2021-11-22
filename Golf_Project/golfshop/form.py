from django.forms import ModelForm
from .models import *

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

##customer order form