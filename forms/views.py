import datetime
from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
from django.contrib import messages
from .models import Subscriber

# Create your views here.
def index(request):
    context = { 'message': 'Welcome to django'}
    return render(request, 'index.html', {"context": context})

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def filter_demo(request):
    context = {
        "my_string": "Hello World",
        "my_date": datetime.date(2025, 6, 18),
        "long_string": "This is a long string to be displayed entirely",
    }
    return render(request, 'filters.html', context)

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form}) 

def error_404(request, exception):
    return render(request, '404.html', status=404)   

from django.shortcuts import render, redirect
from .forms import BlogForm  # Ensure your BlogForm is correctly imported

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)  # Modify the blog object if needed
            blog.save()
            return redirect('blog_list')  # Redirect after successful submission
    else:
        form = BlogForm()

    return render(request, 'add_blog.html', {'form': form})


def blog_list(request):
	blogs = Blog.objects.all()
	context = {'blogs': blogs}
	return render(request, 'blog_list.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
        return redirect('subscribe')  # redirect after processing POST

    return render(request, 'subscribe.html')
