from django.contrib import admin
from .models import ReviewPost
from .models import Comment

# Register your models here.
admin.site.register(ReviewPost)
admin.site.register(Comment)
