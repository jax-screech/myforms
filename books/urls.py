from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet) # to register the BookViewSet with the router

urlpatterns = [
    path('', include(router.urls)), # to include the router's URLs in the urlpatterns
]
