from django.contrib import admin
from .models import Booking


# Register your models here.

# Registers booking model with admin display, filter and search
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'check_in', 'check_out', 'number_of_guests',
        'total_cost', 'created_on'
        )
    list_filter = ('check_in', 'check_out',)
    search_fields = ('name', 'email')


admin.site.register(Booking, BookingAdmin)
