from django.urls import path
from . import views

# URL patterns for booking the shack, viewing bookings, and managing them
urlpatterns = [
    path('', views.book_shack, name='book_shack'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/',
         views.cancel_booking, name='cancel_booking'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]
