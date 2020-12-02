# django-project
First Django project

# Install django
```
python -m pip install Django
```

# Check which version is installed
```
python -m django --version
```

# Start dev server
```
python manage.py runserver
# Specific port
python manage.py runserver 8080
```

# Structure
* The outer `TP_Django/` root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
* The inner `mysite/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
* `mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
* `mysite/settings.py:` Settings/configuration for this Django project. Django settings will tell you all about how settings work.
* `mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
* `mysite/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
* `mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

# Create an application
```
python manage.py startapp todo
```

##### Projects vs. apps
> What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.


## Write a view

Open the file todo/views.py
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

To create a URLconf in the polls directory, create a file called `urls.py
```
from django.urls import path

from . import views`

urlpatterns = [
    path('', views.index, name='index'),
]
```

The next step is to point the root URLconf at the polls.urls module. In `TP_Django/urls.py`, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),
]
```

Check if route is working :
```
http://127.0.0.1:8000/todo/
```

# Database configuration
File : `TD_Django/settings.py`

Default values with SQLite 3 :
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
Could be configure with another database type :
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
More details [here](https://docs.djangoproject.com/fr/3.1/intro/tutorial02/). 

# Execute database migration

```python manage.py migrate```
> The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your TP_Django/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies. If you’re interested, run the command-line client for your database and type \dt (PostgreSQL), SHOW TABLES; (MariaDB, MySQL), .schema (SQLite), or SELECT TABLE_NAME FROM USER_TABLES; (Oracle) to display the tables Django created.

# Activating models

`TP_DJANO/settings.py`
```
INSTALLED_APPS = [
    'todo.apps.TodoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
Create a migration :
```
python manage.py makemigrations todo
```
Should return something like :
```
Migrations for 'todo':
  todo/migrations/0001_initial.py
    - Create model Task
```
