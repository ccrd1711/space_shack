from django.apps import AppConfig


# Config for bookings app, set default auto field and app name
class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'
