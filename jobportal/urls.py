"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alljob', views.view_all_jobs, name="viewall"),
    path('add', views.add_job, name="add"),
    path('edit/<rid>', views.edit_job, name="edit"),
    path('delete/<rid>', views.delete_job, name="delete"),
    path('filterbybatch', views.filterbybatch, name="filterbybatch"),
    path('filterbylocation', views.filterbylocation, name="filterbylocation"),
    path('filterbydegree', views.filterbydegree, name="filterbydegree"),
    path('sortbydate', views.sortbydate, name="sortbydate"),
    path('getjob/<rid>', views.get_job, name="getjob"),
    path('search', views.search_job, name="searchjob"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('', views.index, name="index"),
    
    path('signup/', views.candidate_signup, name='candidate_signup'),
    path('login/', views.candidate_login, name='candidate_login'),
    path('logout/', views.candidate_logout, name='candidate_logout'),
    
    # path('', views.job_list, name='job_list'),
    path('apply_for_job/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('applications/', views.job_applications, name='job_applications'),
    path('applications/<int:application_id>/accept/', views.accept_job_application, name='accept_job_application'),
    path('applications/<int:application_id>/reject/', views.reject_job_application, name='reject_job_application'),

]
