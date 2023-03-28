from django import forms
from .models import customers,drone_booking

class customersForm(forms.ModelForm):
    class Meta:
        model=customers
        fields="__all__"

class drone_bookingForm(forms.ModelForm):
    class Meta:
        model=drone_booking
        fields="__all__"