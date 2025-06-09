from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.
def book_shack(request):
    form = BookingForm(request.POST or None)    #

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request,
                           "You must be logged in to book the Space Shack.")
        elif form.is_valid():
            booking = form.save(commit=False)
            nights = (booking.check_out - booking.check_in).days
            booking.total_cost = nights * 5000
            booking.user = request.user
            booking.save()
            return render(request,
                          'bookings/confirmation.html', {'booking': booking})

    return render(request, 'bookings/booking_form.html', {'form': form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user).order_by('-created_on')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    print("VIEW HIT:", request.method)
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        print("DELETING BOOKING")
        booking.delete()
        return redirect('my_bookings')
    return render(request,
                  'bookings/confirm_cancel.html', {'booking': booking})


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            updated_booking = form.save(commit=False)
            nights = (
                updated_booking.check_out - updated_booking.check_in).days
            updated_booking.total_cost = nights * 5000
            updated_booking.save()
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)

    return render(request,
                  'bookings/edit_booking.html',
                  {'form': form, 'booking': booking})
