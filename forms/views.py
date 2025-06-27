from django.shortcuts import render, redirect
from .forms import BlogForm

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
    return render(request, 'add_form.html', {'form': form})    