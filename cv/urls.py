from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_homepage, name='cv_homepage'),
    # personal details
    path('personaldetails/edit', views.pd_edit, name='pd_edit'),
    # experience
    path('experiences/<int:pk>/edit', views.exp_edit, name='exp_edit'),
    path('experiences/<int:pk>/remove', views.exp_remove, name='exp_remove'),
    path('experiences/new', views.exp_new, name='exp_new'),
    # qualifications
    path('qualifications/<int:pk>/edit', views.qual_edit, name='qual_edit'),
    path('qualifications/<int:pk>/remove', views.qual_remove, name='qual_remove'),
    path('qualifications/new', views.qual_new, name='qual_new'),
    # projects
    path('projects/<int:pk>/edit', views.proj_edit, name='proj_edit'),
    path('projects/<int:pk>/remove', views.proj_remove, name='proj_remove'),
    path('projects/new', views.proj_new, name='proj_new')
]
