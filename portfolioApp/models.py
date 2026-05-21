from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):

    def __str__(self):
        return self.username

class PersonalInfoModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=20,null=True)
    profession = models.CharField(max_length=50, null=True)
    short_bio = models.CharField(max_length=150,null=True)
    about = models.TextField(null=True)
    additionalink = models.CharField(max_length=150,null=True)
    address = models.TextField(null=True)
    image = models.ImageField(upload_to='media/profile',null=True)

    def __str__(self):
        return self.name or 'none'
    

class WorkExperienceModel(models.Model):

    company_name = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    achivements = models.TextField(null=True)

    def __str__(self):
        return self.company_name
    
class EducationModel(models.Model):

    institution_name = models.CharField(max_length=100,null=True)
    degree = models.CharField(max_length=100,null=True)
    result = models.FloatField(null=True)
    passing_year = models.DateField(auto_now_add=False)
    

    def __str__(self):
        return self.institution_name
    
class ProjectModel(models.Model):
    title = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="media/project",null=True)
    technologies_used = models.CharField(max_length=200,null=True)
    github_link = models.CharField(max_length=200,null=True)
    live_demo_link = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
class TechnicalModel(models.Model):
  
    skill_name= models.CharField(null=True, max_length=50)    
    description = models.TextField(null=True)
    level = models.FloatField(null=True)
    icon = models.ImageField(upload_to="media/skill",null=True)

    def __str__(self):
        return self.skill_name