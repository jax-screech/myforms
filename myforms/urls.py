"""
URL configuration for myforms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django_registration.backends.one_step.views import RegistrationView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('forms.urls')),
    path('api/', include('products.urls')),
    path('api/', include('books.urls')),
    path('', include('forms.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('pdf_reader/', include('pdf_reader.urls')),
    path('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
]

handler404 = 'forms.views.error_404'
#if settings.DEBUG:
   # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])