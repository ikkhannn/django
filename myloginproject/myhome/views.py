from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# from django.contrib.auth import login,authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,CreateNewList, CreateNewProject 
from .models import ProjectsList,Projects
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.
# from django.views.generic import TemplateView

# class HomePageView(TemplateView):
#     template_name = 'home.html'

# inside views.py

@login_required
def index(request, id):
    ls = ProjectsList.objects.get(id=id)

    if ls in request.user.projectslist.all():
        if request.method == "POST":

            form = CreateNewProject(request.POST)
            if form.is_valid():
                t = form.cleaned_data["project_title"]
                d = form.cleaned_data["project_description"]
                new_record = ls.projects_set.create(project_title=t,project_description=d,pub_date=timezone.now())
                new_record.save()
            # return redirect("/home")

            # if request.POST.get("newItem"):
            #     title = request.POST.get("title")
            #     description = request.POST.get("description")

            #     if len(title) > 2 and len(description) > 5 :
            #         new_item=ls.projects_set.create(project_title=title,project_description=description,pub_date=timezone.now())
            #         new_item.save()
                    
            #         print(ls)
            #         print(title,description)
            #     else:
            #         print("invalid")
            else:
                print("invalid")
        else:
            form = CreateNewProject()

            

        return render(request, "list.html", {"form":form,"ls":ls})

    return render(request, "home.html")

def home(request):
    return render(request, 'home.html')


def register(request):
    # request.user (user ki saari details yahan se access karsakte hain)
    if(request.user.is_authenticated):
        return HttpResponseRedirect('accounts/login')
    else:
        if request.method=="POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("/home")
        else:

            form= RegisterForm()
        return render(request,"registration/register.html",{"form":form})

@login_required
def view(request):
    return render(request,"view.html",{})

@login_required
def create(request):

    if request.method == "POST":

        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ProjectsList(name=n)
            t.save()
            request.user.projectslist.add(t)  # adds the to do list to the current logged in user
            return HttpResponseRedirect("projectslist/%i" %t.id)
    else:

        form = CreateNewList()

    return render(request, "create.html", {"form":form})

def project_update(request, pk):

    if(request.method == "GET"):
        if pk == 0 :
            form=CreateNewProject()
        else:
            project= Projects.objects.get(pk=pk)
            form= CreateNewProject(instance=project)
        return render(request,"list.html",{'form':form})
    else:
        if pk==0:
            form=CreateNewProject(request.POST)
        else:
            project= Projects.objects.get(pk=pk)
            form= CreateNewProject(request.POST,instance=project)
        if form.is_valid():
            form.save()
            print("done")
        return redirect('/projectslist/edit/{}'.format(pk))

    # project = get_object_or_404(Projects, pk=pk)
    # form = CreateNewProject(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/')
    # return render(request,'viewlist', {'form':form})

# def project_delete(request, pk):
#     book= get_object_or_404(Book, pk=pk)    
#     if request.method=='POST':
#         book.delete()
#         return redirect('book_list')
#     return render(request, template_name, {'object':book})