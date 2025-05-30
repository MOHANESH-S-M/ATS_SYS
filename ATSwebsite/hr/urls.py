from django.urls import path
from . import views


urlpatterns = [
    path("",views.home , name= 'home'),
    path("create-job/",views.createjob,name='create-job'),
    path("editjob/<slug:slug>/",views.editjob,name = "editjob"),
    path("deletejob/<slug:slug>",views.deletejob,name='deletejob'),
]
