from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms

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


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Пароли не совпадают')
        return cleaned


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                form.add_error(None, 'Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def lab7_page(request):
    return render(request, 'lab7.html')

