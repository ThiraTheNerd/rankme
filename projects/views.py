# .Rest framework imports
# type:ignore
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project, Rate, Profile
from .serializer import ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required
from .forms import RatingForm, PostProjectForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# ........
from django.shortcuts import redirect, render

# Create your views here.
sorted(zip(score, name), reverse=True)[:3]


def index(request):
    try:
        projects = Project.objects.all()
        print(projects)
    except ObjectDoesNotExist:
        projects = None
    
    
    sorted(zip(score, name), reverse=True)[:3]

    if request.method == "POST":
        form = PostProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user
            project.save()
        else:
            form = PostProjectForm()
    else:
        form = PostProjectForm()
    ctx = {
        "projects": projects,
        "project_form": form,
       
    }
    return render(request, "index.html", ctx)


def profile(request, username):
    user = User.objects.get(username=username)
    try:
        user_profile = Profile.objects.get(user=user.id)
    except ObjectDoesNotExist:
        return Http404
    ctx = {"user_profile": user_profile}
    return render(request, "profile.html", ctx)

def view_project(request, id):
    try:
        project = Project.objects.get(pk=id)
    except ObjectDoesNotExist:
        raise Http404
    rating = Rate.objects.filter(user=request.user, project=project).first()
    user = request.user
    rating_status = None
    if rating is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project
            rate.save()
            project_ratings = Rate.objects.filter(project=project)

            design_rates = [d.design for d in project_ratings]
            design_average = sum(design_rates) / len(design_rates)

            content_rates = [c.content for c in project_ratings]
            content_avg = sum(content_rates) / len(content_rates)

            usability_rates = [u.usability for u in project_ratings]
            usability_avg = sum(usability_rates) / len(usability_rates)

            total_score = (design_average + content_avg + usability_avg) / 3
            rate.design_average = round(design_average, 2)
            rate.usability_avg = round(usability_avg, 2)
            rate.content_avg = round(content_avg, 2)
            rate.total_score = round(total_score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)

    else:
        form = RatingForm()

    ctx = {
        "project": project,
        "rating_form": form,
        "rating_status": rating_status,
        "user": user,
    }

    return render(request, "project/project.html", ctx)

@login_required(login_url="/accounts/login/")
def create_project(request):
    if request.method == "POST":
        form = PostProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user
            project.save()
            return redirect('index')
    else:
        form = PostProjectForm()
    ctx ={
        "form": form
    }

    return render(request, "project/new_project.html", ctx)



def update_project(request):
    pass


def update_project(request):
    pass


def delete_project(request):
    pass


class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)


class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
