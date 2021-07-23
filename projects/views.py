# .Rest framework imports
# type:ignore
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializer import ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required

# ........
from django.shortcuts import render

# Create your views here.

def index(request):
    projects = Project.objects.all()
    ctx = {"projects": projects}
    return render(request, "index.html", ctx)

@login_required(login_url='/accounts/login/')
def view_project(request, id):
    try:
        project = Project.objects.get(pk=id)
    except ObjectDoesNotExist:
        raise Http404
    ctx = {"project": project}

    return render(request, "project/project.html", ctx)


def create_project(request):
    pass


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
