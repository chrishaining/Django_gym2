# Notes

This document contains some of the thoughts and questions I had during the creation of the Django Gym app. The purpose of the document is to improve my understanding of the concepts I am using, and to compare the way Django works with other technologies (in particular React).

27/Jan/2020
I'm trying to get my head around the admin site and how this could connect with the main app. In the admin site, I've created a group of users called Members. These members can view and edit certain fields, but I'm not sure how that translated to the code for the app.

Tables - I'm playing with the Bootstrap table properties. At the moment I'm trying to change the widths of the columns. I've seen that using w-auto inside the class expression will automatically set the width to accommodate the contents, but it isn't working.  
    

How to select an instructor from the list on the home page and view the full details? 
In the home page, the instructor table shows the names of each instructor. Each row represents a different instructor. The user hovers over a row in the Instructors table. When they click on the row, they should be able to see more details on the chosen instructor (e.g. profile, sessions they can teach). This could either be a pop-up window or a new page. 

Some ideas I found online:
<button type="submit" value={{excel_path}} onclick="location.href='{% url 'downloadexcel' %}'" name='mybtn2'>Download Excel file</button>

<form action='actionUrl' method='GET'>
<button type='submit'> sort me</button>
</form>


#locations/urls.py
# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns("locations.views",
    url(r"^$", "location_list", name="location_list"),
    url(r"^(?P<slug>[^/]+)/$", "location_detail",
        name="location_detail"),
    url(r"^(?P<slug>[^/]+)/popup/$", "location_detail_popup",
        name="location_detail_popup...


Possible code for dealing with many-to-many aspect of sessions:
Inside models.py - 
    class Session(models.Model): 
    ...
    participants = models.ManyToManyField(Member)

Then when you want to add a member to a session (not sure which file this would go in):
    session.participants.add(new_member)

# Retrieving objects
one_entry = Entry.objects.get(pk=1)
[Django docs](https://docs.djangoproject.com/en/3.0/topics/db/queries/#field-lookups)


<!-- I have added the seeds for the sessions. They didn't work (due to a foreign key problem), and it's not a problem I need to focus on (as I should be able to add sessions via the admin site). -->
  <!-- {
        "model": "gym.Session",
        "fields": {
            "title": "Pilates",
            "description": "The perfect class for building core strength.",
            "level": "Low",
            "capacity": 10
        }
    }, -->

// {
    //     "model": "gym.Session",
    //     "fields": {
    //         "title": "Pump Up the Jam",
    //         "description": "The perfect class for beginners to get moving with some cheesy dance moves.",
    //         "level": "Low",
    //         "capacity": 20
    //     }
    // },

    // {
    //     "model": "gym.Session",
    //     "fields": {
    //         "title": "Kick ass",
    //         "description": "For people who want to take their fitness to a new level. Do you think you can handle it?",
    //         "level": "High",
    //         "capacity": 10
    //     }
    // }

## 2nd February 2020
I'm still trying to open a new path from the home page to an instructor page. I tried using the template used in the [Django docs](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#writing-more-views). It is doing something, because when I type the following url path - http://localhost:8000/gym/1/instructor_details/ - it displays some text. However, it's not exactly what I want.