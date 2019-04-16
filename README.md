# Web Programming Practice
Practice playground of the subject Web Programming, IT KMITL.

<img src="https://www.fullstackpython.com/img/logos/django.png" width="60%">

## Guide

### Creating Django Project

#### Recommended Method

Create project in PyCharm Professional. Python interpreter will be automatically set.

#### Alternate Method

Type `django-admin startproject <project_name>` in Terminal. This might needs to set Python interpreter path manually. In case the previous method fails, this method can be used.

### Starting a Server

Type `python3 manage.py runserver [port]` in Terminal while in the project directory. If port is not defined, a server will be opened in port 8000 by default.

### Creating Django Applications

Type `python3 manage.py startapp <app_name>` in Terminal

After that, add your new application to *INSTALLED_APPS* in *settings.py*

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    <app_name>
]
```

### Setting Up MySQL Database

1. Config *DATABASES* in *settings.py*

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

4. Add database in Sequel Pro, must matches your *<database_name>* configuration in *settings.py*.

### Migration

Type `python3 manage.py makemigrations <app_name>` make migrations by reading *models.py* of a certain application. Similar to git commit.

Type `python3 manage.py migrate` to migrate database models. Similar to git push.

### Static Files

Add the following code to *settings.py*, where you can replace *'static'* with other static file path.

```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, <path>),
]
```

#### Example

```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```


### Django Admin

Type `python3 manage.py createsuperuser` in Terminal. Username and password can be used in *127.0.0.1:8000/admin/* route.

### Permission Redirect

If user attempts to visit a path without permission, user will be redirected to another path. In this case is the login page. Where you can add the following code to *settings.py*.

```
LOGIN_URL = <redirected_path>
```

#### Example

```
LOGIN_URL = '/polls/login/'
```
