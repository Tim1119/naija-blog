from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from apps.profiles.models import Profile
from apps.posts.models import Article
from django.contrib import messages
from django.http import Http404
# Create your views here.


@login_required()
@require_http_methods('POST')
def comment_create_view(request):
    article_id = request.POST.get('article_id')
    article_slug = request.POST.get('article_slug')
    current_user_profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            article = get_object_or_404(Article, pkid=article_id)
            if article.slug == article_slug:
                instance = form.save(commit=False)
                instance.author = current_user_profile
                instance.article = article
                form.save()
                messages.success(request, 'comment has been created succesfully')
                return redirect('article:article-detail', slug=article_slug)
        else:
            messages.error(request,'comment can not be created due to an error')
            return redirect('article:article-detail', slug=article_slug)



@login_required
@require_http_methods('POST')
def comment_delete_view(request):
    comment_slug = request.POST.get('comment_slug')
    article_slug = request.POST.get('article_slug')
    if request.method == 'POST':
        # current_user_profile = get_object_or_404(Profile, user=request.user)
        comment = get_object_or_404(Comment,slug=comment_slug)
        # article = get_object_or_404(Article,slug=article_slug)  
        if comment.author.user == request.user:
            comment.delete()
            messages.success(request, 'comment has been deleted succesfully')
            return redirect('article:article-detail', slug=article_slug)
        else:
            return Http404("This comment was not created by you. Hence you can't delete it")
    else:
        messages.error(request, 'sorry an error occured.')
        return redirect('article:article-detail', slug=article_slug)
