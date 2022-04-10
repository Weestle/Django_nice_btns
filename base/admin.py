from django.contrib import admin
from .models import Task
from mptt.admin import MPTTModelAdmin

admin.site.register(Task)
