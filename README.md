# Agenda - Django Project

A simple yet functional agenda API build with Django.

### CRUD / Models
* Contact
* ToDo

Make sure to set the proper username and password for your database in `settings.py`.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'agenda',
        'USER': 'MYUSERNAME',
        'PASSWORD': 'MYPASSWORD',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

To run it, type `python manage.py runserver` in your terminal of the Django project.

The server will start running the server at `localhost port 8000 (127.0. 0.1:8000)`.

### Screenshots
![Contacts list](https://github.com/no7sag/django-agenda/blob/master/preview/ss1.jpg)
![Contact details](https://github.com/no7sag/django-agenda/blob/master/preview/ss2.jpg)
![To do list](https://github.com/no7sag/django-agenda/blob/master/preview/ss3.jpg)
