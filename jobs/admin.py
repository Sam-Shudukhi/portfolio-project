from django.contrib import admin

# Register your models here.
from .models import Job
from blog.models import Blog
# display the Job app in the admin panel
admin.site.register(Job)
admin.site.register(Blog)
