from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.shortcuts import get_object_or_404, redirect
from .models import ReviewPost, Like
from .models import Comment

# landing page
def index(request):
    return render(request, 'index.html')

# Actual blog view
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

    user_liked = review.likes.filter(user=request.user).exists()

    if request.method == 'POST':
        if 'like' in request.POST:
           
            if not user_liked:
                Like.objects.create(user=request.user, post=review)

            return redirect('review_detail', review_id=review.id)
   
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
        'form': form,
        'user_liked': user_liked,
        'total_likes': review.likes.count(),
    })

@login_required
def toggle_like(request, review_id):
    review = get_object_or_404(ReviewPost, id=review_id)
    user = request.user
    liked = Like.objects.filter(user=user, post=review)

    if liked.exists():
        liked.delete()  # User already liked it, so unlike
    else:
        Like.objects.create(user=user, post=review)  # Add like

    return redirect('review_detail', review_id=review.id)

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(ReviewPost, id=review_id)

    if review.author != request.user:
        return HttpResponseForbidden("You can't edit this review.")

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', review_id=review.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(ReviewPost, id=review_id)

    if review.author != request.user:
        return HttpResponseForbidden("You can't delete this review.")

    if request.method == 'POST':
        review.delete()
        return redirect('review_list')

    return render(request, 'reviews/confirm_delete_review.html', {'review': review})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        return HttpResponseForbidden("You can't edit this comment.")

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('review_detail', review_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'reviews/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        return HttpResponseForbidden("You can't delete this comment.")

    if request.method == 'POST':
        review_id = comment.post.id
        comment.delete()
        return redirect('review_detail', review_id=review_id)

    return render(request, 'reviews/confirm_delete_comment.html', {'comment': comment})