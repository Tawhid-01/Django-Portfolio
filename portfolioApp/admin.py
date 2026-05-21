from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserModel)
admin.site.register(PersonalInfoModel)
admin.site.register(WorkExperienceModel)
admin.site.register(EducationModel)
admin.site.register(ProjectModel)
admin.site.register(TechnicalModel)

