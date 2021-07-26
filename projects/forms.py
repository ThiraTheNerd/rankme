from django import forms
from django.db.models import fields

from .models import Profile, Project, Rate

class RatingForm(forms.ModelForm):
  class Meta:
    model = Rate
    fields = ["content", "usability", "design"]

class PostProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ["name", "details", "project_image", "site_url"]