from django import forms
from .models import ReviewPost

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewPost
        fields = ['title', 'content', 'featured_image']
