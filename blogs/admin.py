from django.contrib import admin

# Register your models here.
from blogs.models import MyBlog, Reply

admin.site.register(MyBlog)
admin.site.register(Reply)
