from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article, Category, Tags
from .forms import ArticleForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from apps.comments.forms import CommentForm
from django.views.decorators.http import require_http_methods
from apps.profiles.models import Profile
# Create your views here.


class ArticleHomeView(ListView):
    model = Article
    template_name = "articles/index.html"
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(status='Published', approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        recent_articles = Article.objects.all().filter(
            status='Published',)[::5]
        tags = Tags.objects.all()
        context['categories'] = categories
        context['recent_articles'] = recent_articles
        context['tags'] = tags
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        categories = Category.objects.all()
        recent_articles = Article.objects.all().exclude(
            slug=self.kwargs['slug'])[::5]
        tags = Tags.objects.all()
        context['categories'] = categories
        context['recent_articles'] = recent_articles
        context['tags'] = tags
        context['form'] = form
        return context


class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('article:home')
    success_message = 'Article has been created succesfully'
    template_name = 'articles/create-article.html'

    def get_form_kwargs(self):
        kwargs = super(ArticleCreateView, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Article()
        kwargs['instance'].author = self.request.user.profile
        return kwargs


class ArticleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/update.html"
    success_message = "Article was updated successfully"
    success_url = reverse_lazy('article:home')

    def get_object(self, queryset=None):
        obj = super(ArticleUpdateView, self).get_object()
        if not obj.author.user == self.request.user:
            raise PermissionDenied(
                "You don't have permission to update an article you didn't create")
        return obj


class ArticleDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Article
    success_message = "Article was deleted successfully"
    success_url = reverse_lazy('article:home')

    def get_object(self, queryset=None):
        obj = super(ArticleDeleteView, self).get_object()
        if not obj.author.user == self.request.user:
            raise PermissionDenied(
                "You don't have permission to delete an article you didn't create")
        return obj


def display_article_by_category_view(request, slug):
    searched_category = get_object_or_404(Category, slug=slug)
    all_categories = Category.objects.exclude(slug=slug)
    recent_articles = Article.objects.all()[::5]
    tags = Tags.objects.all()

    articles = Article.objects.filter(category=searched_category)
    return render(request, 'articles/searched-category.html', {'articles': articles, 'categories': all_categories, "recent_articles": recent_articles, 'tags': tags, 'searched_category': searched_category})


@require_http_methods('POST')
def search_article(request):
    if request.method == "POST":
        search_query = request.POST.get('search_query')
        articles = Article.objects.filter(title__icontains=search_query)
        all_categories = Category.objects.all()
        recent_articles = Article.objects.all()[::5]
        tags = Tags.objects.all()
        return render(request, 'articles/searched-query.html', {'articles': articles, 'categories': all_categories, "recent_articles": recent_articles, 'tags': tags, 'searched_query': search_query})


class ArticleDraftsListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles/drafts.html"
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        profile = get_object_or_404(Profile, user=self.request.user)
        return qs.filter(status='Draft', author=profile, approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        recent_articles = Article.objects.all().filter(
            status='Published',)[::5]
        tags = Tags.objects.all()
        context['categories'] = categories
        context['recent_articles'] = recent_articles
        context['tags'] = tags
        return context
