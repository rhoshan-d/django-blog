from django import forms
from .models import Comment, VehicleProject

class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Comment
        fields = ('body',)

class VehicleProjectForm(forms.ModelForm):
    class Meta:
        model = VehicleProject
        fields = ['title', 'make', 'model', 'year', 'description', 'vehicle_image']