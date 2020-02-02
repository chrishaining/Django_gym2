from django.urls import path
from . import views

# I think views.index is the index method defines in views.py
urlpatterns = [
    path('', views.index, name='index'),
    path('member_details/', views.member, name='member_details'),
    path('instructor_detail/<int:pk>', views.InstructorDetailView.as_view(), name='instructor_detail')
    # path('instructor_details/<int:instructor_pk>', views.instructor, name='instructor_details')
    # path('/instructor_details/<int:instructor_id>/', views.instructor, name='instructor_details')
]