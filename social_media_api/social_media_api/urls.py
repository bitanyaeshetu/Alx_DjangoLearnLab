"""
URL configuration for social_media_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # Make sure the accounts URLs are included
]

# social_media_api/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),  # This line should include the posts URLs
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as auth_views  # <-- Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', auth_views.obtain_auth_token),  # <-- Add this URL pattern for token authentication
    path('api/', include('posts.urls')),  # Existing URL pattern for your API
]

from rest_framework.authtoken import views as auth_views

urlpatterns = [
    # Add this URL to handle token creation
    path('api/token/', auth_views.obtain_auth_token),  # This is the endpoint to get a token
    # other URL patterns
]

# social_media_api/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),  # Ensure the posts app URLs are included
    path('api/token/', obtain_auth_token),  # This line is for obtaining the token
]

