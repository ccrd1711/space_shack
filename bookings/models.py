from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User 

user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #optional foreign key to User model

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number_of_guests = models.PositiveIntegerField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(default=timezone.now)

    def clean(self):
        if self.number_of_guests > 2:
            raise ValidationError("Number of guests cannot exceed 2.")

        if self.check_in and self.check_out:
            if self.check_in >= self.check_out:
                raise ValidationError("Check-out date must be after check-in date.")
            if self.check_in.date() < timezone.now().date():
                raise ValidationError("Check-in date cannot be in the past.")

            overlapping_bookings = Booking.objects.filter(
            check_out__gt=self.check_in,
            check_in__lt=self.check_out,
            )
            if self.pk:
                overlapping_bookings = overlapping_bookings.exclude(pk=self.pk)

            if overlapping_bookings.exists():
                raise ValidationError("Sorry, these dates are already booked by another guest.")

        
    def __str__(self):
        return f"Booking for {self.name} from {self.check_in} to {self.check_out}"
    
