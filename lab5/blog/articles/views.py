from django.shortcuts import render, redirect
from django.http import Http404
from .models import Article
from .forms import ArticleForm


def archive(request):
    posts = Article.objects.all().order_by('-created_date')
    return render(request, 'archive.html', {'posts': posts})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article.html', {'post': post})


def create_post(request):
    if not request.user.is_authenticated:
        raise Http404
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            Article.objects.create(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                author=request.user
            )
            return redirect('archive')
    else:
        form = ArticleForm()
    return render(request, 'create_post.html', {'form': form})
