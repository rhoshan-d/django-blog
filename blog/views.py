from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import Post, Comment, VehicleProject, ProjectLike
from .forms import CommentForm, VehicleProjectForm
import time


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)

            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    })


def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating comment!'
            )
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own comments!'
        )
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class VehicleProjectList(View):
    def get(self, request):
        projects = VehicleProject.objects.filter(status=1).order_by(
            '-created_on'
        )
        return render(
            request, 'blog/project_list.html', {'projects': projects}
        )


def vehicle_project_detail(request, slug):
    project = get_object_or_404(VehicleProject, slug=slug)
    liked = False
    if request.user.is_authenticated:
        liked = project.is_liked_by(request.user)
    return render(request, 'blog/project_detail.html', {
        'project': project,
        'liked': liked
    })


@login_required
def create_vehicle_project(request):
    if request.method == 'POST':
        form = VehicleProjectForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle_project = form.save(commit=False)
            vehicle_project.owner = request.user
            
            base_slug = slugify(vehicle_project.title)
            unique_suffix = f"{request.user.username}-{int(time.time())}"
            vehicle_project.slug = f"{base_slug}-{unique_suffix}"
            
            vehicle_project.status = 1
            vehicle_project.save()
            return redirect('project_detail', slug=vehicle_project.slug)
    else:
        form = VehicleProjectForm()
    return render(request, 'blog/project_form.html', {'form': form})


class VehicleProjectDelete(LoginRequiredMixin, DeleteView):
    model = VehicleProject
    template_name = 'blog/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')


@login_required
def edit_vehicle_project(request, slug):
    vehicle_project = get_object_or_404(VehicleProject, slug=slug)
    if request.method == 'POST':
        form = VehicleProjectForm(
            request.POST,
            request.FILES,
            instance=vehicle_project
        )
        if form.is_valid():
            vehicle_project = form.save(commit=False)
            vehicle_project.status = 1
            vehicle_project.save()
            return redirect('project_detail', slug=vehicle_project.slug)
    else:
        form = VehicleProjectForm(instance=vehicle_project)
    return render(request, 'blog/project_form.html', {'form': form})


@login_required
def like_project(request, slug):
    project = get_object_or_404(VehicleProject, slug=slug)
    like, created = ProjectLike.objects.get_or_create(
        user=request.user,
        project=project
    )
    
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
        
    return JsonResponse({
        'liked': liked,
        'likes_count': project.likes.count()
    })
