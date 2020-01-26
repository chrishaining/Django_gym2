from django.contrib import admin
from django.contrib.admin import sites
from gym.models import *
# Register your models here.
admin.site.register(Member)
admin.site.register(Session)
admin.site.register(Instructor)
# reset the View Site link in the admin page (the default is to go to root, which I didn't want)
sites.AdminSite.site_url = '/gym/'