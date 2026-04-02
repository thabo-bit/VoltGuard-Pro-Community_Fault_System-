from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # These 'include' lines tell Django to look inside each app's own urls.py
    path('', include('dashboard.urls')),       
    path('reports/', include('reports.urls')), 
    path('ops/', include('ops_portal.urls')),  
]