# Notes

This document contains some of the thoughts and questions I had during the creation of the Django Gym app. The purpose of the document is to improve my understanding of the concepts I am using, and to compare the way Django works with other technologies (in particular React).

27/Jan/2020
I'm trying to get my head around the admin site and how this could connect with the main app. In the admin site, I've created a group of users called Members. These members can view and edit certain fields, but I'm not sure how that translated to the code for the app.

Tables - I'm playing with the Bootstrap table properties. At the moment I'm trying to change the widths of the columns. I've seen that using w-auto inside the class expression will automatically set the width to accommodate the contents, but it isn't working.  
    


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