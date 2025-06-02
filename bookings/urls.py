from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_shack, name='book_shack'),
    path('my/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]

