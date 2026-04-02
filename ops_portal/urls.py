from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.ops_login, name='ops_login'),
    path('dashboard/', views.ops_dashboard, name='ops_dashboard'),
    path('logout/', views.ops_logout, name='ops_logout'),  # <--- CHECK THIS LINE
    path('update-fault/<int:fault_id>/', views.update_fault_status, name='update_fault_status'),
]