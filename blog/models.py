from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User 
# Create your models here.
class Blog(models.Model): 
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=360)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-detail', kwargs={'blog_id': self.id})
# blogs = [
#     Blog('1', '1', datetime(2025, 10, 21)),
#     Blog('2', '2', datetime(2025, 10, 21)),
#     Blog('3', '3', datetime(2025, 10,20)),
# ]    