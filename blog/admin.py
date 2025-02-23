from django.contrib import admin
from .models import Post, Comment, VehicleProject  # Import the new model
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)


@admin.register(VehicleProject)
class VehicleProjectAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'owner',
        'make',
        'model',
        'year',
        'status',
        'created_on'
    )
    search_fields = ['title', 'description', 'make', 'model']
    list_filter = ('status', 'created_on', 'make', 'model', 'year')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)
