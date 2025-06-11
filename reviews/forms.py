from django import forms
from .models import ReviewPost
from .models import Comment


# Form for submitting a review, including title, content, and rating
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewPost
        fields = ['title', 'content', 'rating']
        widgets = {
            'rating': forms.Select(
                choices=[
                    (i, f"{i} Stars")
                    for i in range(1, 6)
                ]
            ),
        }


# Form for submitting a comment with styled textarea input
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Write your comment here...',
                'rows': 4,
                'style': 'resize: vertical;'
            }),
        }
