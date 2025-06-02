from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_shack, name='book_shack'),
]