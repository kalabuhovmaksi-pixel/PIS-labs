Лабораторная работа №3
======================

Краткое описание
----------------
Создание блога на Django: модель статьи, админ-интерфейс и вывод списка записей через представление и шаблон.

Реализовано
-----------
- создан Django-проект `blog` и приложение `articles`
- добавлена модель `Article` (title, author, text, created_date) и метод `get_excerpt`
- подключена модель к админке через `ArticleAdmin` и `admin.site.register`
- выполнены миграции и добавлены тестовые статьи через админ-панель
- создано представление `archive`, возвращающее список статей `Article.objects.all()`
- добавлен шаблон `archive.html` со списком всех статей (заголовок, автор, дата, краткий текст)

Запуск
------
cd lab3/blog
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
