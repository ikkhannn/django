from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=12,null=True,blank=True)
    status = models.CharField(max_length=10, default="active")

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()