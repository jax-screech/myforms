from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# Create user and save to the database
# user = User.objects.create_user('myusername', 'myemail@email.com', 'mypassword')
# # Update the fields and save
# user.first_name = 'Joseph'
# user.last_name = 'Kwanusu'
# user.save()

# class Blog(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def __str__(self):
#         return self.title
    
class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    @classmethod
    def published(cls):
        return cls.objects.filter(is_published=True)    


class Editor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='editors')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=20, unique=True)
    mobile = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    