from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from . import models


class ArticleListView(ListView):
    model = models.Article
    template_name = 'articles/article_list.html'


class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'articles/article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Article
    fields = ['title', 'body', ]
    template_name = 'articles/article_edit.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'articles/article_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('article_list')


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'articles/article_new.html'
    fields = ['title', 'body', ]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    template_name = 'articles/comment_new.html'
    fields = ['comment', ]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = models.Article.objects.get(slug=self.kwargs.get('slug'))
        return super().form_valid(form)


class SearchResultsListView(ListView):
    models = models.Article
    template_name = 'articles/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return models.Article.objects.filter(
            Q(title__icontains=query) |
            Q(author__username__icontains=query) |
            Q(body__icontains=query)
        )
