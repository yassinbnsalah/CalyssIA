from django.contrib.auth.models import AbstractUser
from django.db import models

class RUser(AbstractUser):
    # Add related_name for groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Use a distinct related name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Use a distinct related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    
    # Additional fields
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
