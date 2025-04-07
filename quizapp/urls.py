from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),           # Main homepage (lists quiz topics)
    path('questions/', include('questions.urls')),  # Quiz questions
    path('analytics/', include('analytics.urls')),  # Analytics and results
    path('users/', include('users.urls')),     # User-specific pages and actions
    path('accounts/', include('allauth.urls')), # Login, Signup, and authentication
]
