from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ReviewPost
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required 
from .forms import CommentForm
from django.shortcuts import get_object_or_404, redirect

# Test route view
# def my_blog(request):
#    return HttpResponse("Hello, space blog!")

# Actual blog view
@login_required 
def review_list(request):
    reviews = ReviewPost.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})

@login_required
def review_detail(request, review_id):
    review = get_object_or_404(ReviewPost, id=review_id)
    comments = review.comments.all().order_by('-created_on')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = review
            comment.author = request.user
            comment.save()
            return redirect('review_detail', review_id=review.id)
    else:
        form = CommentForm()

    return render(request, 'reviews/review_detail.html', {
        'review': review,
        'comments': comments,
        'form': form
    })