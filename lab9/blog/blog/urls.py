from django.contrib import admin
from django.urls import path
from articles import views as articles_views

urlpatterns = [
    path('', articles_views.archive, name='home'),
    path('admin/', admin.site.urls),
    path('archive/', articles_views.archive, name='archive'),
    path('article/new/', articles_views.create_post, name='create_post'),
    path('article/<int:article_id>/', articles_views.get_article, name='article'),

    path('login/', articles_views.login_view, name='login'),
    path('register/', articles_views.register_view, name='register'),

    path('lab7/', articles_views.lab7_page, name='lab7'),
]
