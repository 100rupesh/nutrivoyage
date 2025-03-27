from django.contrib import admin
from django.urls import path, include  # include is used to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('clients.urls')),  # Include the app's URL configuration
]