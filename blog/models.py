from django.db import models

# Create your models here.
class Blog(models.Model): 
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=360)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

# blogs = [
#     Blog('1', '1', datetime(2025, 10, 21)),
#     Blog('2', '2', datetime(2025, 10, 21)),
#     Blog('3', '3', datetime(2025, 10,20)),
# ]    