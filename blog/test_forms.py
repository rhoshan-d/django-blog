import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .forms import CommentForm, VehicleProjectForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")


class TestVehicleProjectForm(TestCase):

    def test_form_is_valid(self):
        image_path = './static/images/default.jpg'
        with open(image_path, 'rb') as image:
            form_data = {
                'title': 'Project Title',
                'slug': 'project-title',
                'make': 'Car Make',
                'model': 'Car Model',
                'year': 2020,
                'description': 'Project Description',
            }
            file_data = {
                'vehicle_image': SimpleUploadedFile(
                    name='default.jpg',
                    content=image.read(), content_type='image/jpeg')
            }
            form = VehicleProjectForm(data=form_data, files=file_data)
            self.assertTrue(form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid_missing_fields(self):
        form_data = {
            'title': '',
            'make': 'Car Make',
            'model': 'Car Model',
            'year': 2020,
            'description': 'Project Description',
            'vehicle_image': 'path/to/image.jpg'
        }
        form = VehicleProjectForm(data=form_data)
        self.assertFalse(form.is_valid(), msg="Form is valid")

    def test_form_is_invalid_invalid_year(self):
        form_data = {
            'title': 'Project Title',
            'make': 'Car Make',
            'model': 'Car Model',
            'year': 'invalid_year',
            'description': 'Project Description',
            'vehicle_image': 'path/to/image.jpg'
        }
        form = VehicleProjectForm(data=form_data)
        self.assertFalse(form.is_valid(), msg="Form is valid")

    def test_form_is_invalid_missing_image(self):
        form_data = {
            'title': 'Project Title',
            'make': 'Car Make',
            'model': 'Car Model',
            'year': 2020,
            'description': 'Project Description',
        }
        form = VehicleProjectForm(data=form_data)
        self.assertFalse(form.is_valid(), msg="Form is valid")
