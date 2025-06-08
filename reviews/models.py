from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
from django.utils import timezone 


# Create your models here.
class ReviewPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True, max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="review_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    rating = models.IntegerField(
        default=5,
        choices=[(i, f"{i} Stars") for i in range(1, 6)],
        help_text="Select a rating from 1 to 5 stars"
    )

    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    @property
    def total_likes(self):
        return self.likes.count()

    
class Comment(models.Model):
    post = models.ForeignKey(ReviewPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ReviewPost, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'post')  # ensures user can only like a post once

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"
