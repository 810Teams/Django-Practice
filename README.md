# Web Programming Practice
Practice playground of the subject Web Programming, IT KMITL.

<br>
<img src="https://www.fullstackpython.com/img/logos/django.png" width="60%">
<br>

[![forthebadge](https://forthebadge.com/images/badges/compatibility-pc-load-letter.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-js.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-vue.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)

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

### Enable CORS

Add the following code to *settings.py*, make sure this part of code stays above *INSTALLED_APPS*.

```
CORS_ORIGIN_ALLOW_ALL=True
```

Next, add *'corsheaders'* to *INSTALLED_APPS* in *settings.py*.

```
INSTALLED_APPS = [
    <existing_apps>,
    'corsheaders',
]
```

Lastly, add *'corsheaders.middleware.CorsMiddleware'* to *MIDDLEWARE* in *settings.py*.

```
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    <existing_middlewares>
]
```
