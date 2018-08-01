from django.db import models
from django.contrib.auth.models import User

class BlogType(models.Model):
    type_name = models.CharField(max_length=32)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    author = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING)
    blog_type = models.ForeignKey(BlogType, to_field='id', on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']