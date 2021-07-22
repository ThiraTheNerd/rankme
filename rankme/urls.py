# type:ignore
from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views 
from django_registration.backends.one_step.views import RegistrationView
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("projects.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^logout/$', views.LogoutView.as_view(), {"next_page": '/'}) ,
    url(r"^api-token-auth/", obtain_auth_token),
]

