from rest_framework import viewsets, filters
from .models import Book
from .sterializers import BookSerializer
from rest_framework.pagination import PageNumberPagination

class BookPagination(PageNumberPagination):
    page_size = 5 # set the default number of items returned per page in a paginated API
    page_size_query_param = 'page_size' # control how many items appear per page
    max_page_size = 100 #then set the maximum number of items that can be returned in a single page

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')  # Fetch all books, ordered by their title
    serializer_class = BookSerializer # Use the BookSterializer to convert data to JSON(for computers to understand)
    pagination_class = BookPagination # enable the bBookPagination class to paginate the results
    filter_backends = [filters.SearchFilter] # Allow filtering of the search results
    search_fields = ['title', 'author'] # to allow the user to search by title and author fields