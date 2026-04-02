from django.shortcuts import render
from .models import FaultReport

def dashboard_view(request):
    # Fetch all reports from the database
    reports = FaultReport.objects.all().order_by('-created_at')
    
    # Simple stat for the top card
    total_active = reports.exclude(status='RESOLVED').count()
    
    context = {
        'reports': reports,
        'total_active': total_active,
    }
    # Notice the path: 'dashboard/dashboard.html'
    return render(request, 'dashboard/dashboard.html', context)