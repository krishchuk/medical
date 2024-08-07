## Medical

### Сайт компании медицинской диагностики 

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Bootstrap](https://img.shields.io/badge/-Bootstrap-464646?style=flat-square&logo=Bootstrap)](https://getbootstrap.com/)


### Технологии:
- python 3.12
- django 5.0.7
- PostgreSQL


### Установка и запуск проекта:

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/krishchuk/medical.git
    ```
2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
3. Настройте переменные окружения в файле `.env` по примеру из `.env_sample`:
    ```
    SECRET_KEY=your-secret-key
    ...
    ```
4. Выполните миграции:
    ```bash
    python manage.py migrate
    ```
5. Загрузите фикстуры с данными:
    ```bash
    python manage.py loaddata имя_фикстуры.json
    ```
6. Создайте суперпользователя:
    ```bash
    python manage.py csu
    ```
7. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```
8. Приложение доступно по адресу http://127.0.0.1:8000/.


### Автор проекта:
https://github.com/krishchuk/