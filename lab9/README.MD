Лабораторная работа №9
======================

Краткое описание
----------------
Реализация параллакс-эффекта на странице архива блога с использованием jQuery: несколько фоновых слоёв, двигающихся с разной скоростью при прокрутке.

Реализовано
-----------
- создан отдельный макет страницы архива (`lab9_for_parallax`) на основе существующего шаблона
- добавлена обёртка `.parallax-wrapper` и фоновые слои `.parallax-layer` в `archive.html`
- описаны стили параллакса в `article.css` (градиентные фоны, фиксированное позиционирование слоёв)
- реализован скрипт `parallax.js` на jQuery с обработчиком `$(window).scroll(...)`
- смещение фоновых слоёв рассчитывается на основе `scrollTop` и применяется через `transform: translateY(...)`
- подключены все необходимые статические файлы: `jquery.js`, `highlight-post.js`, `logo-zoom.js`, `parallax.js`

Запуск
------
cd lab9/blog
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
