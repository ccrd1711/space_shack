from django import forms
from .models import ReviewPost

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewPost
        fields = ['title', 'slug', 'content', 'featured_image']
