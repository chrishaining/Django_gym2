from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.CharField(max_length=255, default="Not given") # for ease, leave this as a string for now, though some sort of date time would be better
    age = models.IntegerField(default=0) # leave this as a direct input for now, though I could make the age dependent on dob
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    FITNESS_LEVEL_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High')
    ]
    fitness_level = models.CharField(max_length=6,
        choices=FITNESS_LEVEL_CHOICES,
        default=MEDIUM,)
    goal = models.CharField(max_length=255, default="General fitness")
    attendance = models.IntegerField(default=0) # later, this will be based on their sign-ups for sessions
    sessions = [] # leave this as blank for now, but later I will want to add a method to add sessions.

class Instructor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #classes_they_can_teach = []
    profile = models.TextField()
    
class Session(models.Model):
    title = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, default="", on_delete=models.CASCADE)