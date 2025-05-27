from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # URL for user signup
]