from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('filters/', views.filter_demo, name="filters"),
    # path('blogs/', views.blog_list, name="blogs"),
    # path('subscribe/', views.subscribe, name="subscribe"),
    
]
