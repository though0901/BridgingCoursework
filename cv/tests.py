from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.test import TestCase
from cv.models import *


# Create your tests here.
class HomePageTest(TestCase):
    def test_cv_page_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv_homepage.html')

    def test_can_go_to_blog_and_returns_correct_code(self):
        response = self.client.get('/')
        # the status code is ok
        self.assertEqual(response.status_code, 200)

    def test_can_add_delete_qualification(self):
        Qualification.objects.create(institution="school1", grades="A")
        Qualification.objects.create(institution="school2", grades="A*")

        self.assertTrue(Qualification.objects.count(), 2)

        # check not saving the same object twice
        q1, q2 = get_object_or_404(Qualification, pk=1), get_object_or_404(Qualification, pk=2)
        self.assertEqual(q1.institution, "school1")
        self.assertEqual(q2.institution, "school2")

        q1.delete()
        q2.delete()

        self.assertEqual(Qualification.objects.count(), 0)

    def test_can_add_delete_projects(self):
        Project.objects.create(project_name="proj1", project_description="desc1")
        Project.objects.create(project_name="proj2", project_description="desc2", github_link="github.com")

        self.assertTrue(Project.objects.count(), 2)

        p1, p2 = get_object_or_404(Project, pk=1), get_object_or_404(Project, pk=2)
        self.assertEqual(p1.project_name, "proj1")
        self.assertEqual(p2.project_name, "proj2")

        p1.delete()
        p2.delete()

        self.assertEqual(Project.objects.count(), 0)

    def test_can_add_delete_experience(self):
        Experience.objects.create(company="comp1", description="desc1")
        Experience.objects.create(company="comp2", description="desc2")

        self.assertTrue(Experience.objects.count(), 2)

        e1, e2 = get_object_or_404(Experience, pk=1), get_object_or_404(Experience, pk=2)
        self.assertEqual(e1.company, "comp1")
        self.assertEqual(e2.company, "comp2")

        e1.delete()
        e2.delete()

        self.assertEqual(Experience.objects.count(), 0)