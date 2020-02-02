from django.shortcuts import render
from django.http import HttpResponse
from gym.models import *
from django.contrib.auth.decorators import login_required
from django.views import generic

# Create your views here.
def index(request):
    sessions = Session.objects.all()
    instructors = Instructor.objects.all()
    return render(request, "gym/index.html", locals())

# InstructorDetailView.as_view
def instructor(request, instructor_pk):
    instructor = Instructor.objects.get(instructor_pk)
    return render(request, "gym/instructor_details.html", locals())

# def instructor(request, instructor_id):
#     # return HttpResponse("You've selected instructor %s." % instructor_id)
#     instructor = Instructor.object.get(instructor_id)
#     return render(request, "gym/instructor_details/<int:instructor_id>", locals())

# class InstructorDetailView(generic.DetailView):
#     model = Instructor



# when the user logs in, they should be taken to the member_details page, which shows their personal details as well as their sessions. I am not sure how to access the Member instance (without getting all the other members, too)
@login_required
def member(request):
 members = Member.objects.all()
 return render(request, "gym/member_details.html", locals())