from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfoModel
        fields = "__all__"
        exclude = ['user']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperienceModel
        fields = "__all__"
     
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'

class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields = "__all__"

       
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = "__all__"
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'



class TechnicalForm(forms.ModelForm):
    class Meta:
        model = TechnicalModel
        fields = "__all__"
   
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'