from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=32, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    read_time = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    