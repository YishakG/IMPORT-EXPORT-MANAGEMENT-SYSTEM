from django.contrib import admin
from .models import User
from .models import Message
from .models import Notification

admin.site.register(Message)
admin.site.register(Notification)
# Register your models here.
