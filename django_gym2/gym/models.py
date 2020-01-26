from django.db import models

# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # for ease, leave this as a string for now, though some sort of date time would be better
    dob = models.CharField(max_length=255, default="Not given")
    # leave this as a direct input for now, though I could make the age dependent on dob
    age = models.IntegerField(default=0)
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
    # later, this will be based on their sign-ups for sessions
    attendance = models.IntegerField(default=0)
    # leave this as blank for now, but later I will want to add a method to add sessions.
    sessions = []

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Instructor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #classes_they_can_teach = []
    profile = models.TextField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Session(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(
        default="Please call 0300 45 45 for more info")

    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    LEVEL_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High')
    ]
    level = models.CharField(max_length=6,
                             choices=LEVEL_CHOICES,
                             default=MEDIUM,)

    capacity = models.IntegerField(default=15)

    instructor = models.ForeignKey(
        Instructor, default="", on_delete=models.CASCADE)
    members = []

    def __str__(self):
        return self.title
