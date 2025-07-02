from django.urls import path
from . import views
from .views import StudentView



urlpatterns = [
    path('', views.index, name='index'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
<<<<<<< HEAD
    #path('filters/', views.filter_demo, name="filters"),
    path('blogs/', views.blog_list, name="blogs"),
    # path('subscribe/', views.subscribe, name="subscribe"),
    path('basic/', StudentView.as_view()),
    path('basic/<int:id>/', StudentView.as_view()),
    path('basic/<int:id>/update/', StudentView.as_view()),
=======
    path('filters/', views.filter_demo, name="filters"),
    path('blogs/', views.blog_list, name="blogs"),
    path('subscribe/', views.subscribe, name="subscribe"),
    
>>>>>>> ae066601e81b303a82bfd355d29c0407101ec3c3
]
