# Web Programming Practice
Practice playground of the subject Web Programming, IT KMITL.

<img src="https://www.fullstackpython.com/img/logos/django.png" width="60%">

## Guide

### Creating Django Project

1. Create project in PyCharm Professional.
2. In Terminal, change directory to your recently created project.
3. Type `django-admin startproject <project_name>` in Terminal.

### Starting a Server

Type `python3 manage.py runserver [port]` in Terminal while in the project directory. If port is not defined, a server will be opened in port 8000 by default.

### Creating Django Applications

Type `python3 manage.py startapp <app_name>` in Terminal.

### Setting Up MySQL Database

1. Config `DATABASES` in `settings.py`

    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': <database_name>,
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
    ```

2. Start MySQL server by typing `brew services start mysql` in Terminal.

3. Open Sequel Pro and connect.

4. Add database in Sequel Pro, must matches your `<database_name>` configuration in `settings.py`.

### Migration

Type `python3 manage.py makemigrations <app_name>` apply migrations by reading `models.py` of a certain application. Similar to git commit.

Type `python3 manage.py migrate` to migrate database models. Similar to git push.
