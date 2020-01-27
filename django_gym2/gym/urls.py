from django.urls import path
from . import views

# I think views.index is the index method defines in views.py
urlpatterns = [
    path('', views.index, name='index'),
    path('member_details/', views.member, name='member_details'),
    path('instructor/<int:pk>', views.InstructorDetailView.as_view(), name='instructor_details'),

]