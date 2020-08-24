from django.db import models

# Create your models here.
from django.utils import timezone


class PersonalDetails(models.Model):
    name = models.CharField(default='', max_length=20)
    date_of_birth = models.DateField(default=timezone.now)
    # maybe just want to make this 11 only?
    email_address = models.CharField(default='', max_length=100)


class Qualification(models.Model):
    institution = models.CharField(default='', max_length=100)
    grades = models.TextField(default='')


class Experience(models.Model):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    company = models.CharField(default='', max_length=100)
    description = models.TextField(default='')


class Project(models.Model):
    project_name = models.CharField(default='', max_length=100)
    project_description = models.TextField(default='')
    github_link = models.CharField(default='', max_length=100, blank=True, null=True)
