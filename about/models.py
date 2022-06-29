from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=20)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
