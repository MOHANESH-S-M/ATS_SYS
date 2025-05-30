from django.urls import path
from . import views
"""
urlpatterns = [
    path("<slug:slug>/",views.apply_to_job,name="apply-job"),
    path("<slug:slug>/",views.apply_success,name="apply-success"),
]"""

urlpatterns = [
    path("apply/<slug:slug>/", views.apply_to_job, name="apply-job"),
    path("success/", views.apply_success, name="apply-success"),
]
