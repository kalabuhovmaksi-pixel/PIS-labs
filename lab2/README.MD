## Лабораторная работа №2

### Краткое описание

Создание первого web-приложения на **Django**: проект с одной страницей, выводящей простой текст/HTML с помощью представления и шаблона.

### Реализовано

- создан Django‑проект `helloworld` с помощью `django-admin.py startproject`
- создано приложение `flatpages` командой `python manage.py startapp flatpages`
- настроен маршрут в `urls.py` на представление `home`
- представление `home` сначала возвращает простой `HttpResponse`, затем рендерит HTML‑шаблон `index.html`
- создан шаблон `index.html` с заголовками, абзацами, списками и таблицей
- подключена директория `templates` и настроен рендер страниц через `render`

### Запуск

```bash
cd lab2/helloworld
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
