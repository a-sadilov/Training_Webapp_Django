# Training_Webapp_Django

Сайт для создания кастомных программ тренировок, их редактирования, удаления, изменения, а также добавления тренировок в сетку календаря и отслеживания всех прошедщих и предстоящих событий.
Присутствует возможность регистрации, аутентификации и авторизации.
Реализован API с использованием Rest Framework. В процессе переход View на Vue фреймворк для реализации SPA.


# Запуск на локальной машине:


## Перейдем в папку проекта:

* ```cd training_configurator```

## Установка сторонних зависимостей:

* ```pip install -r requirements.txt```

## Создание миграций:

* ```python manage.py makemigrations```

## Применение миграций:

* ```python manage.py migrate```

## Запуск сервера:

* ```python manage.py runserver```
