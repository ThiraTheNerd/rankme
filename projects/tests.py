from django.test import TestCase
from .models import Project, Profile, User

# Create your tests here.


class ProjectTestClass(TestCase):
    """
    Projects test method
    """

    def setUp(self):

        self.user1 = User(username="manny")
        self.user1.save()

        self.project = Project(title="igclone")
        self.project.save_project()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Project))

    def test_save_method(self):
        """
        test image by save
        """
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)


class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username="manny")
        self.profile = Profile.objects.create(
            user=self.user, bio="I am manny", phone_number=9999907
        )

    def test_isinstance(self):
        self.assertTrue(isinstance(self.user, Profile))
