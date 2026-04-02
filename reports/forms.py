from django import forms
from .models import FaultReport

class FaultReportForm(forms.ModelForm):
    # Defining specific categories for a community power/utility system
    CATEGORY_CHOICES = [
        ('', 'Select Fault Category'),
        ('STREET_LIGHT', 'Street Light Outage'),
        ('POWER_SURGE', 'Power Surge / Voltage Issue'),
        ('CABLE_THEFT', 'Suspected Cable Theft'),
        ('POTHOLE', 'Pothole / Road Damage'),
        ('WATER_LEAK', 'Major Water Leak'),
        ('OTHER', 'Other Community Issue'),
    ]

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full p-4 bg-white/50 border border-slate-200 rounded-2xl outline-none focus:border-orange-500 font-bold text-slate-700 transition-all cursor-pointer'
        })
    )

    class Meta:
        model = FaultReport
        fields = ['category', 'street_name', 'description', 'latitude', 'longitude']
        
        widgets = {
            'street_name': forms.TextInput(attrs={
                'class': 'w-full p-4 bg-white/50 border border-slate-200 rounded-2xl outline-none focus:border-orange-500 font-bold text-slate-700 placeholder:text-slate-400 transition-all',
                'placeholder': 'Type to search address...',
                'id': 'id_street_name' # Critical for the Google JavaScript to find it
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-4 bg-white/50 border border-slate-200 rounded-2xl outline-none focus:border-orange-500 font-medium text-slate-600 placeholder:text-slate-300 transition-all',
                'rows': 4,
                'placeholder': 'Provide details (e.g., "The pole is leaning" or "Sparking wires")'
            }),
            # Hidden inputs so they don't clutter the stylish UI
            'latitude': forms.HiddenInput(attrs={'id': 'id_latitude'}),
            'longitude': forms.HiddenInput(attrs={'id': 'id_longitude'}),
        }