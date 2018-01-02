from django.shortcuts import render
from .models import MyBlog
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from blogs.forms import MyBlogForm, PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

@login_required
def titles(request):
    #titles = MyBlog.objects.order_by('add_time')
    titles = MyBlog.objects.filter(owner=request.user).order_by('add_time')
    context = {'titles': titles}
    return render(request, 'blog/titles.html',context)

@login_required
def title(request, title_id):
    title = MyBlog.objects.get(id=title_id)
    if title.owner != request.user:
        raise Http404
    context = {'title': title}
    return render(request, 'blog/title.html', context)

@login_required
def new_blog(request):
    if request.method != 'POST':
        form = MyBlogForm()
    else:
        form = MyBlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('blogs:titles'))
    context = {'form': form}
    return render(request, 'blog/new_blog.html', context)

@login_required
def edit_blog(request, title_id):
    blog = MyBlog.objects.get(id=title_id)
    title = blog.title
    if blog.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = PostForm(instance=blog)
    else:
        form = MyBlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("blogs:title", args=[blog.id]))
    context = {'blog': blog, 'form': form, 'title': title}
    return render(request, 'blog/edit_blog.html', context)
