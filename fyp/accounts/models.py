from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('institution', 'Institution'),
        ('student', 'Student'),
        ('verifier', 'Verifier'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')
    phone = models.CharField(max_length=15, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    # Institution approval fields
    is_approved = models.BooleanField(default=False, help_text="Indicates if institution is verified and approved")
    approval_date = models.DateTimeField(blank=True, null=True, help_text="Date when institution was approved")
    approved_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_institutions', help_text="Admin who approved this institution")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Auto-approve admin and staff users
        if self.user_type == 'admin' or self.is_staff or self.is_superuser:
            self.is_approved = True
            if not self.approval_date:
                from django.utils import timezone
                self.approval_date = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    class Meta:
        ordering = ['-created_at']

