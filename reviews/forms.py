from django import forms
from .models import ReviewPost
from .models import Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewPost
        fields = ['title', 'content', 'featured_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']