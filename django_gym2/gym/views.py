from django.shortcuts import render
from django.http import HttpResponse
from gym.models import *


# Create your views here.
def index(request):
    sessions = Session.objects.all()
    instructors = Instructor.objects.all()
    return render(request, "gym/index.html", locals())