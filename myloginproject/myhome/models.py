from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProjectsList(models.Model):
    

    user = models.ForeignKey(User,default=None, on_delete=models.CASCADE,related_name="projectslist",null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Projects(models.Model):
    
    projectslist = models.ForeignKey(ProjectsList, on_delete=models.CASCADE,null=True)
    project_title=models.CharField(max_length=200)
    project_description = models.CharField(max_length=500)
    pub_date=models.DateTimeField('date published',auto_now_add=True,null=True)
    

    def __str__(self):
        return self.project_title