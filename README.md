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
