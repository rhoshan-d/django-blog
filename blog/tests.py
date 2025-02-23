from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class GeneralSiteTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )

    def test_home_page_status_code(self):
        """Test that homepage returns 200 status code"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        """Test that about page returns 200 status code"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_projects_page_status_code(self):
        """Test that projects page returns 200 status code"""
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)

    def test_login_required_project_creation(self):
        """Test that unauthenticated users can't access project creation"""
        response = self.client.get(reverse('project_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/accounts/login/?next=/vehicles-projects/create/'
        )

    def test_authenticated_project_creation_access(self):
        """Test that authenticated users can access project creation"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('project_create'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """Test that correct templates are being used"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'blog/index.html')
