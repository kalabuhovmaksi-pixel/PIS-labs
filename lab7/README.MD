Лабораторная работа №7
======================

Краткое описание
----------------
Добавление JavaScript-логики на страницу архива: сворачивание/разворачивание постов, работа с DOM и отладка скриптов в браузере.

Реализовано
-----------
- подключён скрипт `helloworld.js` к шаблону `archive.html` через статические файлы
- реализована кнопка «Свернуть» для каждого поста с обработчиком `addEventListener('click', ...)`
- скрытие и показ автора, даты и текста статьи через изменение `style.display`
- использование DOM-методов (`getElementsByClassName`, `parentElement`, `innerHTML`)
- реализация функций форматирования и вывода списка студентов (аналог Python-версии `groupmates`) на JavaScript
- отладка скриптов в Google Chrome (Console, Source, breakpoints, просмотр переменных)

Запуск
------
cd lab7/blog
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
