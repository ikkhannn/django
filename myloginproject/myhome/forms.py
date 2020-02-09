from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProjectsList,Projects

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields=["username","email","password1","password2"]


class CreateNewList(forms.ModelForm):
    class Meta:
        model = ProjectsList
        fields=["name"]
#   name=forms.CharField(label="Name",max_length=200)
    
class CreateNewProject(forms.ModelForm):
    class Meta:
        model = Projects
        fields=["project_title","project_description"]

    # project_title=forms.CharField(label="Project Name",max_length=200)
    # project_description=forms.CharField(label="Project Description",max_length=500)