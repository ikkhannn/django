from django.urls import path,include
# from .views import HomePageView
from . import views


urlpatterns = [
#    path('', HomePageView.as_view(), name='home'),
    path('projectslist/<int:id>', views.index, name='index'),
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('createlist',views.create,name='create'),
    path('viewlist',views.view,name='view'),
    path('viewlist/delete/<int:pk>',views.projectslist_delete,name='projectslist_delete'),
    path('projectslist/delete/<int:pk>',views.project_delete,name='delete'),
    path('projectslist/edit/<int:pk>', views.project_update,name='project_update'),
    path('searchprojects/',views.search_project_type,name='search_project_type')

]

