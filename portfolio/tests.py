from django.test import TestCase, Client
from django.urls import reverse
from .models import Profile, Skill, Project, Experience, ContactMessage


class PortfolioViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(
            name="Gourav Berwal",
            title="Data Analyst",
            email="gouravberwal003@gmail.com",
            phone="+91 9516637166"
        )
        self.skill = Skill.objects.create(
            name="Python",
            icon_image="images/Python.png",
            category="languages",
            order=1
        )
        self.project = Project.objects.create(
            title="Amazon Clone",
            category="filter-se",
            tech_stack="HTML | CSS",
            bullet_1="Sample bullet",
            image="images/Amazon.png",
            order=1
        )
        self.experience = Experience.objects.create(
            role="Campus Ambassador",
            company="Acmegrade",
            date_range="2023",
            logo="images/acmegrade_logo.png",
            points="Point 1\nPoint 2",
            order=1
        )

    def test_homepage_loads(self):
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gourav Berwal")
        self.assertContains(response, "Python")
        self.assertContains(response, "Amazon Clone")
        self.assertContains(response, "Acmegrade")

    def test_contact_form_submission_ajax(self):
        response = self.client.post(
            reverse('portfolio:contact_submit'),
            data={
                'name': 'Test User',
                'email': 'test@example.com',
                'phone': '1234567890',
                'message': 'Hello from test',
                'ajax': 'true'
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ContactMessage.objects.filter(name='Test User').exists())

    def test_contact_form_submission_standard(self):
        response = self.client.post(
            reverse('portfolio:contact_submit'),
            data={
                'name': 'Standard User',
                'email': 'standard@example.com',
                'phone': '9876543210',
                'message': 'Hello from standard post'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ContactMessage.objects.filter(name='Standard User').exists())

    def test_resume_endpoint_serves_pdf(self):
        response = self.client.get(reverse('portfolio:resume'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertIn('Gourav_Berwal_Resume.pdf', response['Content-Disposition'])
