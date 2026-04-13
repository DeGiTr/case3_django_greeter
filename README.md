# Кейс 3 — Django-приложение

Приложение позволяет:

- ввести имя пользователя через форму;
- сохранить это имя в базе данных SQLite;
- показать персонализированное приветствие на главной странице;
- обработать ошибку пустого поля;
- использовать CSRF-защиту Django.

## Запуск

```powershell
cd individual_practice\case3_django_greeter
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

После запуска откройте `http://127.0.0.1:8000/`.

## Проверка

```powershell
python manage.py check
python manage.py test
```

## Что важно для задания

- модель содержит одно пользовательское поле: `name`;
- форма защищена через `{% csrf_token %}`;
- пустое имя не сохраняется в базе данных;
- интерфейс стилизован через CSS.
