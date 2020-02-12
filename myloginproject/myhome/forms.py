from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProjectsList,Projects

city_choices = (
    ('karachi','Karachi'),
    ('faisalabad', 'Faisalabad'),
    ('lahore','Lahore'),
    ('islamabad','Islamabad'),
    ('quetta','Quetta'),
)
class RegisterForm(UserCreationForm):

    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    location = forms.CharField(widget=forms.Select(choices=city_choices))
    class Meta:

        model=User
        fields=["username","email","password1","password2"]
        
                
    # def clean(self): 
    #     cleaned_data=super().clean()

    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')

    #     # extract the username and text field from the data 
  
    #     # conditions to be met for the username length 
    #     if password1 != password2:
    #         self.add_error('password1','passwords are not same')
  
        # return any errors if found 
        


class CreateNewList(forms.ModelForm):
    name= forms.CharField(widget=(forms.TextInput(attrs={'class':'form-control'})))
    class Meta:
        model = ProjectsList
        fields=["name"]
        

    # def clean_name(self):
    #     data = self.cleaned_data.get('name')

    #     if(data!="ik"):
    #         raise forms.ValidationError('name is not ik')
        
    #     return data

    # def clean(self):
    #     cleaned_data=super().clean()

    #     name=cleaned_data.get("name")

    #     if(name!='ik'):
    #         self.add_error('name','name is not ikkk')

#   name=forms.CharField(label="Name",max_length=200)
    
class CreateNewProject(forms.ModelForm):
    project_title= forms.CharField(label='Project Title',widget=(forms.TextInput(attrs={'class':'form-control'})))
    project_description= forms.CharField(label='Project Title',widget=(forms.TextInput(attrs={'class':'form-control'})))
    class Meta:
        model = Projects
        fields=["project_title","project_description"]

    # project_title=forms.CharField(label="Project Name",max_length=200)
    # project_description=forms.CharField(label="Project Description",max_length=500)