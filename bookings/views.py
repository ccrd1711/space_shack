from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from datetime import timedelta

# Create your views here.
def book_shack(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            nights = (booking.check_out - booking.check_in).days
            booking.total_cost = nights * 5117
            booking.save()
            return render(request, 'bookings/confirmation.html', {'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})