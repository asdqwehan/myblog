from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyBlog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    def __str__(self):
        return self.title

class Reply(models.Model):
    topic = models.ForeignKey(MyBlog)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
