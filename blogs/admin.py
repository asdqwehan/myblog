from django.contrib import admin

# Register your models here.
from blogs.models import MyBlog

admin.site.register(MyBlog)
