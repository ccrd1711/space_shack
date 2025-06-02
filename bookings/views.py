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
        if request.user.is_authenticated:
            booking.user = request.user 
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_on')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('my_bookings')
    return render(request, 'bookings/confirm_cancel.html', {'booking': booking})