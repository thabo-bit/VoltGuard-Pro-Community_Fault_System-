from django.db import models
from django.contrib.auth.models import User
import uuid

class FaultReport(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('DISPATCHED', 'Dispatched'),
        ('REPAIRING', 'Repairing'),
        ('RESOLVED', 'Resolved'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ref_number = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=100) # Increased for longer category names
    description = models.TextField()
    
    # Increased to 255 to store the full "123 Barkly Rd, Homestead, Kimberley, 8301"
    street_name = models.CharField(max_length=255) 
    
    # Coordinates for the Map Pins
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically generate a Ref Number if it's a new report
        if not self.ref_number:
            self.ref_number = f"VG-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ref_number} - {self.street_name}"