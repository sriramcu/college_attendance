"""college_attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from attendance import views as attendance_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('modify/', attendance_views.modify, name='modify'),
    path('check/', attendance_views.check, name='check'),
    path('view_tt/', attendance_views.view_tt, name='view_tt'),
    path('change_tt/', attendance_views.change_tt, name='change_tt'),
    path('detailed/', attendance_views.detailed, name='detailed'),
    path('add_courses/', attendance_views.add_courses, name='add_courses'),
    path('', attendance_views.base, name='base'),
]
