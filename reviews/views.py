from django.shortcuts import render
from django.http import HttpResponse
from .models import ReviewPost

# Test route view
def my_blog(request):
    return HttpResponse("Hello, space blog!")

# Actual blog view
def review_list(request):
    reviews = ReviewPost.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})