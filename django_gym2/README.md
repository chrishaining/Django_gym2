# Django Gym

This is my second attempt at creating a gym app using Django. The scenario is an app that is used by gym members to manage their fitness sessions^. There's also an admin facility that allows an admin-level user (member of gym staff) to edit and delete members, sessions and instructors. Features of the app include:
* member has to login to use the app
* member can view and edit their own profile (e.g. name, weight, height)
* member can view details of a session (e.g. title, date, time, instructor)
* member can view details of each instructor
* the app should use responsive design so that it can be viewed on devices of different sizes (including mobile devices)

^A session is the name used for a fitness class. I didn't use the word "class" in the app since it is a reserved word in Python.

## The main features I wanted to work on are:
* Create a login feature for authorisation
* Enable users to edit details using a form
* Enable users to click on sections of a web page to view/edit them
* I also used this as an oppotunity to practise unit testing of the models

## Languages/packages
* Python 3
* pip
* Django (built with version 3.0)
* Bootstrap 4.0

## To download and run the app
* Set up a virtual environment: `python -m venv .env`
* Open the virtual environment: `source .env/bin/activate`
* install Django: `pip3 install django`
* Clear any existing data in the database: `python manage.py flush`. When prompted, type `yes`
* Populate the database: `python manage.py loaddata seeds.json`
* To run the app: `python manage.py runserver`. Use the local port advised in the script.
* To gain access to the admin function, create a user from the command line: `python manage.py createsuperuser`

# <img src="/static/images/weightlifting.jpg" width="80%" height="200">
