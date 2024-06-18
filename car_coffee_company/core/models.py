# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     USER_TYPES = (
#         ('importer', 'Importer'),
#         ('exporter', 'Exporter'),
#         ('admin', 'Administrator'),
#         ('accountant', 'Accountant'),
#         ('finance_manager', 'Finance Manager'),
#         ('compliance_officer', 'Compliance Officer'),
#     )
#     user_type = models.CharField(max_length=20, choices=USER_TYPES)
#     company_name = models.CharField(max_length=100,default="SIEMS")
#     # last_login = models.DateTimeField(blank=True, null=True)
#     # contact_info = models.JSONField(null=True)
# # core/models.py
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email
# # core/models.py
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
# #     date_joined = models.DateTimeField(auto_now_add=True)
# #     last_login = models.DateTimeField(null=True, blank=True)  # Ensure this field exists

# #     objects = UserManager()

# #     USERNAME_FIELD = 'email'
# #     REQUIRED_FIELDS = []

# #     def __str__(self):
# #         return self.email

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, password, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
#     USER_TYPES = (
#         ('importer', 'Importer'),
#         ('exporter', 'Exporter'),
#         ('admin', 'Administrator'),
#         ('accountant', 'Accountant'),
#         ('finance_manager', 'Finance Manager'),
#         ('compliance_officer', 'Compliance Officer'),)

#     user_type = models.CharField(max_length=20, choices=USER_TYPES)
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(unique=True, null=True, blank=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     # user_type = models.CharField(max_length=50)  # Custom field

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     last_login = models.DateTimeField(blank=True, null=True)  # Include last_login

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.username
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')
        user = self.create_user(username, password,is_staff=True,is_superuser=True)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('importer', 'Importer'),
        ('exporter', 'Exporter'),
        ('admin', 'Administrator'),
        ('accountant', 'Accountant'),
        ('finance_manager', 'Finance Manager'),
        ('compliance_officer', 'Compliance Officer'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    @property
    def user(self):
         return self.user_type