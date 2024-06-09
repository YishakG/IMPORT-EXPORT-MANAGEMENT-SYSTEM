# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPES = (
        ('importer', 'Importer'),
        ('exporter', 'Exporter'),
        ('admin', 'Administrator'),
        ('accountant', 'Accountant'),
        ('finance_manager', 'Finance Manager'),
        ('compliance_officer', 'Compliance Officer'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    company_name = models.CharField(max_length=100)
    contact_info = models.JSONField(null=True)
