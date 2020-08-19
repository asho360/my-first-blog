from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, CV, Experience
from .forms import PostForm
from .forms import CVForm, ExperienceForm


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def cv_home(request):
    cv = CV.objects.all()
    experience = Experience.objects.filter().order_by('start_date')
    return render(request, 'cv/cv_home.html', {'cvs':cv,'experiences':experience})

@login_required
def edit_cv(request):
    cv = get_object_or_404(CV, pk=1)
    if request.method == "POST":
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.save()
            return redirect('cv_home')
    else:
        form = CVForm(instance=cv)   
    return render(request, 'cv/edit_cv.html', {'form': form})

@login_required
def edit_experience(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.save()
            return redirect('cv_home')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'cv/edit_experience.html', {'form': form})

@login_required
def new_experience(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid:
            experience = form.save(commit=False)
            experience.save()
            return redirect('cv_home')
    else:
        form = ExperienceForm()
    return render(request, 'cv/edit_experience.html', {'form': form})

@login_required
def remove_experience(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    experience.delete()
    return redirect('cv_home')