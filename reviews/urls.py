from django.urls import path
from . import views
from .views import add_review 

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('add/', add_review, name='add_review'), 
]
