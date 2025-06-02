from django.urls import path
from . import views
from .views import add_review 

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('add/', add_review, name='add_review'), 
    path('<int:review_id>/', views.review_detail, name='review_detail'),
    path('like/<int:review_id>/', views.toggle_like, name='toggle_like'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
