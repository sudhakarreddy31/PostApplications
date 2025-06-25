from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)     #for SEO in urls in webpage..

    def __str__(self):
        return self.title
    