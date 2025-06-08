from django import forms
from .models import ReviewPost
from .models import Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewPost
        fields = ['title', 'content', 'rating']
        widgets = {
            'rating': forms.Select(choices=[(i, f"{i} Stars") for i in range(1, 6)]), 
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']