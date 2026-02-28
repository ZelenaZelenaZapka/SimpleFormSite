# SimpleFormSite

Простий Django-сайт з формою.

## Як запустити локально
1. `python -m venv venv`
2. `source venv/bin/activate` (або venv\Scripts\activate на Windows)
3. `pip install -r requirements.txt`
4. Створи файл `.env` і додай `SECRET_KEY=твій_ключ` (згенеруй новий!)
5. `python manage.py migrate`
6. `python manage.py runserver`
