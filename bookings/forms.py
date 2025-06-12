from django import forms
from .models import Booking
from django.utils import timezone
from django.core.exceptions import ValidationError
import re


# Booking form with custom validation for guests, email domains, and date logic
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'number_of_guests', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

    # Allow only common email domains
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r".+@.+\.(com|net|org|io|co\.uk|gov|edu)$",
                        email.lower()):
            raise ValidationError(
                    "Please enter a valid email domain (e.g. .com, .org).")
        return email

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        guests = cleaned_data.get('number_of_guests')

        if guests:
            if guests > 2:
                self.add_error('number_of_guests', 'Maximum 2 guests allowed.')
            elif guests < 1:
                self.add_error('number_of_guests',
                               'You must book for at least 1 guest.')

        if check_in and check_out:
            if check_in >= check_out:
                self.add_error('check_out',
                               'Check-out must be after check-in.')

        if check_in:
            if check_in.date() < timezone.now().date():
                self.add_error('check_in', 'Check-in cannot be in the past.')
