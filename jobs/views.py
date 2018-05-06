from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
    # get the jobs to display in home
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
