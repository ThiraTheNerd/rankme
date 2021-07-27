from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField
from url_or_relative_url_field.fields import URLOrRelativeURLField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = HTMLField(max_length=100)
    profile_pic = CloudinaryField(
        default="https://res.cloudinary.com/playboard/image/upload/v1626529829/vjytnast5wblft8xvy9p.jpg",
    )
    full_name = models.CharField(blank=True, max_length=120)
    location = models.CharField(blank=True, max_length=120)

    def __str__(self):
        return self.user


class Project(models.Model):
    name = models.CharField(max_length=50)
    details = HTMLField()
    profile = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    project_image = CloudinaryField()
    site_url = URLOrRelativeURLField(null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save_project(self):
        self.save()

    def update(self):
        self.save()

    def delete(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        projects = cls.objects.filter(title=search_term)
        return projects

    @classmethod
    def get_profile_projects(cls, profile):
        projects = Project.objects.filter(profile__pk=profile)
        return projects

    @classmethod
    def all_posts(cls):
        return cls.objects.all()


rating = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "10"),
)


class Rate(models.Model):
    content = models.IntegerField(choices=rating, null=True, blank=True, default=0)
    usability = models.IntegerField(choices=rating, null=True, blank=True, default=0)
    design = models.IntegerField(choices=rating, null=True, blank=True, default=0)
    contnt_avg = models.FloatField(null=True, blank=True, default=0)
    design_avg = models.FloatField(null=True, blank=True, default=0)
    usability_avg = models.FloatField(null=True, blank=True, default=0)
    total_score = models.FloatField(null=True, default=0)
    project = models.ForeignKey(Project, on_delete=CASCADE, related_name='ratings', null=True)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f"{self.project.name} - {self.total_score}"

    def save_rate(self):
        self.save()

    @classmethod
    def project_rating(cls, id):
        ratings = cls.objects.filter(project_id=id).all()
        return ratings
