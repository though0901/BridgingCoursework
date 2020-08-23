from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from cv.forms import *

'''
for these do edit, new and remove:
    experience 
    qualifications 
    projects
for these just do edit:
    personal details 
'''


# Create your views here.
def cv_homepage(request):
    # want to get all the things here ie all exp, quals, proj and pd's
    pds = PersonalDetails.objects.first()
    quals = Qualification.objects.all()
    exp = Experience.objects.all()
    proj = Project.objects.all()

    return render(request, 'cv_homepage.html', {'pds': pds, 'quals': quals, 'exp': exp, 'proj': proj})


# EXPERIENCE MODIFICATION
@login_required
def exp_edit(request, pk):
    post = get_object_or_404(Experience, pk=pk)
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = ExperienceForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'Edit Experience'})


@login_required
def exp_new(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = ExperienceForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'New Experience'})


@login_required
def exp_remove(request, pk):
    post = get_object_or_404(Experience, pk=pk)
    post.delete()
    return redirect('/cv')


# QUALIFICATION MODIFICATION
@login_required
def qual_edit(request, pk):
    post = get_object_or_404(Qualification, pk=pk)
    if request.method == "POST":
        form = QualificationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = QualificationForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'Edit Qualification'})


@login_required
def qual_new(request):
    if request.method == "POST":
        form = QualificationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = QualificationForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'New Qualification'})


@login_required
def qual_remove(request, pk):
    post = get_object_or_404(Qualification, pk=pk)
    post.delete()
    return redirect('/cv')


# PROJECTS MODIFICATION
@login_required
def proj_edit(request, pk):
    post = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = ProjectForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'Edit Project'})


@login_required
def proj_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = ProjectForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'New Project'})


@login_required
def proj_remove(request, pk):
    post = get_object_or_404(Project, pk=pk)
    post.delete()
    return redirect('/cv')


# PERSONAL DETAILS MODIFICATION THROUGH EDIT ONLY
@login_required
def pd_edit(request):
    post = PersonalDetails.objects.first()
    if request.method == "POST":
        form = PersonalDetailsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = PersonalDetailsForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'Edit Personal Details'})
