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
    path('projectslist/edit/<int:pk>', views.project_update, name='project_update'),

]

