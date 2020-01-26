from django.test import TestCase
from gym.models import *

# Create your tests here.
class MemberTestCase(TestCase):
    def setUp(self):
        self.member1 = Member.objects.create(first_name = "Ron", last_name = "Jones", dob="01/Jan/1986", age=34, weight=70, height=180, fitness_level="High", goal="Lose weight", attendance=10)
    
    def test_member_saved(self):
        self.assertGreater(self.member1.pk, 0)
    
    def test_member_first_name(self):
        self.assertEquals(self.member1.first_name, "Ron")

    def test_member_last_name(self):
        self.assertEquals(self.member1.last_name, "Jones")

    def test_member_dob(self):
        self.assertEquals(self.member1.dob, "01/Jan/1986")

    def test_member_age(self):
        self.assertEquals(self.member1.age, 34)

    def test_member_weight(self):
        self.assertEquals(self.member1.weight, 70)
    
    def test_member_height(self):
        self.assertEquals(self.member1.height, 180)

    def test_member_has_goal(self):
        self.assertNotEquals(self.member1.goal, "")
    
    def test_member_attendance(self):
        self.assertEquals(self.member1.attendance, 10)

    def test_member_starts_with_no_sessions(self):
        self.assertEquals(len(self.member1.sessions), 0)

    def test_member_fitness_level(self):
        self.assertEquals(self.member1.fitness_level, "High")

class SessionTestCase(TestCase):
    def setUp(self):
        self.instructor1 = Instructor.objects.create(first_name = "Mazie", last_name = "Kinsella", profile="I love pilates!")
        self.session1 = Session.objects.create(title = "Pilates", description="Some people love pilates, apparently.", level="High", capacity=9, instructor=self.instructor1)

        self.session2 = Session.objects.create(title = "Yoga", instructor=self.instructor1)
    
    def test_session_saved(self):
        self.assertGreater(self.session1.pk, 0)
    
    def test_session_name(self):
        self.assertEquals(self.session1.title, "Pilates")

    def test_session_can_have_instructor(self):
        self.assertEquals(self.session1.instructor.pk, self.instructor1.pk)

    def test_session_instructor_first_name(self):
        self.assertEquals(self.session1.instructor.first_name, "Mazie")
    
    def test_session_description_default(self):
        self.assertEquals(self.session2.description, "Please call 0300 45 45 for more info")

    def test_session_description(self):
        self.assertEquals(self.session1.description, "Some people love pilates, apparently.")

    def test_session_level_default(self):
        self.assertEquals(self.session2.level, "Medium")

    def test_session_level(self):
        self.assertEquals(self.session1.level, "High")

    def test_session_capacity_default(self):
        self.assertEquals(self.session2.capacity, 15)
    
    def test_session_capacity(self):
        self.assertEquals(self.session1.capacity, 9)
    
    def test_member_starts_with_no_members(self):
        self.assertEquals(len(self.session1.members), 0)

class InstructorTestCase(TestCase):
    def setUp(self):
        self.instructor1 = Instructor.objects.create(first_name = "Mazie", last_name = "Kinsella", profile="I love pilates!")
    
    def test_instructor_saved(self):
        self.assertGreater(self.instructor1.pk, 0)

    def test_instructor_first_name(self):
        self.assertEquals(self.instructor1.first_name, "Mazie")

    def test_instructor_last_name(self):
        self.assertEquals(self.instructor1.last_name, "Kinsella")

    def test_instructor_profile(self):
        self.assertEquals(self.instructor1.profile, "I love pilates!")