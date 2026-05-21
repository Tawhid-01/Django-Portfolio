from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutPage, name='logout'),
    path('personal-info/', personalInfoPage, name='personalInfo'),
    path('work-experience/', workExperiencePage, name='workExperience'),
    path('education/', educationPage, name='education'),
    path('project/', projectPage, name='project'),
    path('technical/', technicalPage, name='technical'),
    path('', dashboardPage, name='dashboard'),
]