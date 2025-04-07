from django.db import models

# Create your models here.
#  models- You define the structure of your database tables using models. Each attribute of the class represents a field in the table.

class Post(models.Model):
    title = models.CharField(max_length=75) 
    body  = models.TextField()
    slug  = models.SlugField()
    date  = models.DateTimeField(auto_now_add=True)
    banner=models.ImageField(default='fallback.png',blank=True)

    def __str__(self):
        return self.title
    
