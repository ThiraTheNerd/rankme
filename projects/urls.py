# type:ignore
from django.conf.urls import include, url
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path("post/<int:id>", views.view_project, name="post_item"),
    path("project/<int:id>", views.view_project, name="view_project"),
    url(r"^api/project/$", views.ProjectList.as_view()),
    url(r"api/project/project-id/(?P<pk>[0-9]+)/$", views.ProjectDescription.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)