import datetime
from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
<<<<<<< HEAD
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404
=======
from django.contrib import messages
from .models import Subscriber
>>>>>>> ae066601e81b303a82bfd355d29c0407101ec3c3

class StudentView(APIView):
    def get(self, request, id=None):
        if id:
            result = Students.objects.get()
            serializers = StudentSerializer(result, many=True)
            return Response({'status': 'success', 'students': serializers.data}, status=200)
        result = Students.objects.all()
        serializers = StudentSerializer(result, many=True)
        return Response({'status': 'success', 'students': serializers.data}, status=200)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            student = Students.objects.get(id=kwargs['id'])
        except Students.DoesNotExist:
            return Response({'status': 'error', 'data': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id):
        result = Students.objects.get(id=id)
        serializer = StudentSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': 'error', 'errors': serializer.errors})
        
    def delete(self,requests, id=None):
        result = get_object_or_404(Students, id=id)
        result.delete()
        return Response({'status': 'success', 'data': 'Record deleted successfully'})
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
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            return redirect('blog_list')
    else:
        form = BlogForm()
<<<<<<< HEAD
    return render(request, 'add_form.html', {'form': form})

def error_404(request, exception):
    return render(request, '404.html', status=404)

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

=======
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
>>>>>>> ae066601e81b303a82bfd355d29c0407101ec3c3
