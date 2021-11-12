from django.forms import ModelForm
from .models import *

from django.contrib.auth.models import Customer


class customerRegisterForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']