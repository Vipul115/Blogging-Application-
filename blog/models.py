from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now) # Use auto_now=True for modifying date every time the post is updated(better for a field like last_modified).auto_now_add=True for seeting immutable date_created field.
    author = models.ForeignKey(User, on_delete= models.CASCADE) # User is the related table. CASCADE=deleting post when user is deleted
