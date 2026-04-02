from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from dashboard.models import FaultReport 

def ops_login(request):
    if request.method == "POST":
        user = request.POST.get('username')
        passw = request.POST.get('password')
        
        if user == "admin" and passw == "admin123":
            request.session['is_logged_in'] = True
            return redirect('ops_dashboard')
        else:
            messages.error(request, "Invalid Technician ID or Access Key")
            
    return render(request, 'ops_portal/login.html')

def ops_dashboard(request):
    if not request.session.get('is_logged_in'):
        return redirect('ops_login')
        
    all_reports = FaultReport.objects.all().order_by('-created_at')
    
    context = {
        'reports': all_reports,
        'total_active': all_reports.filter(status='PENDING').count(),
        'in_progress': all_reports.filter(status='IN_PROGRESS').count(),
    }
    
    return render(request, 'ops_portal/dashboard.html', context)

# --- NEW UPDATE VIEW ---
def update_fault_status(request, fault_id):
    """
    Handles the POST request from the dashboard modal to update status.
    """
    if request.method == "POST":
        # Security: check if logged in
        if not request.session.get('is_logged_in'):
            return redirect('ops_login')

        # Get the specific fault or return 404 if not found
        fault = get_object_or_404(FaultReport, id=fault_id)
        
        # Get the new status from the modal form
        new_status = request.POST.get('status')
        
        # Validate and save
        valid_statuses = ['PENDING', 'IN_PROGRESS', 'RESOLVED']
        if new_status in valid_statuses:
            fault.status = new_status
            fault.save()
            messages.success(request, f"Fault #{fault.id} updated successfully!")
        else:
            messages.error(request, "Invalid status selected.")
            
    return redirect('ops_dashboard')

def ops_logout(request):
    request.session.flush() 
    return redirect('ops_login')