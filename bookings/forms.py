from django import forms
from .models import Booking
from django.utils import timezone
from datetime import timedelta

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'number_of_guests', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        guests = cleaned_data.get('number_of_guests')

        if guests and guests > 2:
            self.add_error('number_of_guests', 'Maximum 2 guests allowed.')

        if check_in and check_out:
            if check_in >= check_out:
                self.add_error('check_out', 'Check-out must be after check-in.')
            if check_in and check_in.date() < timezone.now().date():
                self.add_error('check_in', 'Check-in cannot be in the past.')
