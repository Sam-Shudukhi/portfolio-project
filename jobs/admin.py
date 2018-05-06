from django.contrib import admin

# Register your models here.
from .models import Job
# display the Job app in the admin panel
admin.site.register(Job)
