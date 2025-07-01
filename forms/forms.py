from django import forms
from .models import Blog, Author

class BlogForm(forms.ModelForm):
    # Define the author as a dropdown of authors
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Select an author")
    
    class Meta:
        model = Blog
        fields = ['author', 'image', 'title', 'text', 'is_published']
    def __init__(self, *args, **kwargs ):
        super(BlogForm, self).__init__(*args, **kwargs) 
    
    def clean(self):
        cleaned_data = super().clean() 
        return cleaned_data     