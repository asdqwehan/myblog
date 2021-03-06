from django import forms
from blogs.models import MyBlog, Reply

class MyBlogForm(forms.ModelForm):
    class Meta:
        model = MyBlog
        fields = ('title', 'content')

class PostForm(forms.ModelForm):
    class Meta:
        model = MyBlog
        fields = ('title', 'content')

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']