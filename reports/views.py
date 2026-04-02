import random
from django.shortcuts import render, redirect
from django import forms
from dashboard.models import FaultReport

# Define the form with choices and Tailwind styling
class FaultReportForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Area Outage', 'Area Outage'),
        ('Transformer Issue', 'Transformer Issue'),
        ('Vandalism / Theft', 'Vandalism / Theft'),
        ('Street Light', 'Street Light'),
    ]

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full p-4 bg-slate-50 border-2 border-slate-100 rounded-2xl focus:border-orange-500 outline-none transition cursor-pointer text-slate-700'
        })
    )

    class Meta:
        model = FaultReport
        fields = ['category', 'street_name', 'description']
        widgets = {
            'street_name': forms.TextInput(attrs={
                'class': 'w-full p-4 bg-slate-50 border-2 border-slate-100 rounded-2xl focus:border-orange-500 outline-none transition text-slate-700',
                'placeholder': 'e.g. Barkly Road'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-5 bg-slate-50 border-2 border-slate-100 rounded-2xl focus:border-blue-500 outline-none transition resize-none text-slate-700',
                'placeholder': 'Provide details...',
                'rows': 5
            }),
        }

def report_fault(request):
    if request.method == 'POST':
        form = FaultReportForm(request.POST)
        if form.is_valid():
            # 1. Save the actual data to the database
            new_report = form.save()
            
            # 2. Generate a random reference for the success overlay
            ref_id = random.randint(1000, 9999)
            
            # 3. Stay on page but show the success overlay
            return render(request, 'reports/reports_home.html', {
                'form': FaultReportForm(), # Reset form
                'success': True,
                'reference_id': ref_id
            })
    else:
        form = FaultReportForm()
    
    return render(request, 'reports/reports_home.html', {'form': form})

def report_success(request):
    return render(request, 'reports/reports_home.html')