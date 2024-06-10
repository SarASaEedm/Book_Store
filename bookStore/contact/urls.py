"""
URL configuration for bookStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from contact.views import (contact, aboutus, landing,
                            students_list, student_info, students_landing)


urlpatterns = [
    path('contactpath',contact, name='contactFun'),
    path('aboutus',aboutus,name='aboutus'),
    #path('', landing, name='landing'),
    path('students_list', students_list, name='students_list'),
    path('student_info/<int:id>', student_info, name='student_info'),
    path('index', students_landing,name ='students_landing' ),
]

