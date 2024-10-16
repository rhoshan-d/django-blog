from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import Post, Comment, VehicleProject
from .forms import CommentForm 

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
            messages.add_message(request, messages.SUCCESS, 'Comment submitted and awaiting approval')
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
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class VehicleProjectList(View):
    def get(self, request):
        projects = VehicleProject.objects.filter(status=1).order_by('-created_on')
        return render(request, 'blog/project_list.html', {'projects': projects})


def vehicle_project_detail(request, slug):
    project = get_object_or_404(VehicleProject, slug=slug)
    return render(request, 'blog/project_detail.html', {'project': project})

class VehicleProjectCreate(CreateView):
    model = VehicleProject
    fields = ['title', 'make', 'model', 'year', 'description', 'vehicle_image', 'status']
    template_name = 'blog/project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        
        title = form.cleaned_data.get('title')
        form.instance.slug = slugify(title)
        form.instance.status = 'published'
        
        return super().form_valid(form)

class VehicleProjectUpdate(UpdateView):
    model = VehicleProject
    fields = ['title', 'slug', 'owner', 'make', 'model', 'year', 'description', 'vehicle_image', 'status']
    template_name = 'blog/project_form.html'
    success_url = reverse_lazy('project_list')

class VehicleProjectDelete(DeleteView):
    model = VehicleProject
    template_name = 'blog/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')
