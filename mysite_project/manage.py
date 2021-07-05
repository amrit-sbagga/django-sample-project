#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# from File->settings->project settings -> plus button->django package is installed
# under script django files will be available after this
# django-admin.py is used to create projects
# mysite is created using below command:
# workspace2 > django-admin.py startproject mysite_project

#for running:
# python <path-of-manage.py> runserver
# e.g> python E:\PROGRAMS\PYTHON\workspace2\mysite_project\manage.py runserver
# This will start development server at http://127.0.0.1:8000/

# for starting app
# cd mysite_project
# python E:\PROGRAMS\PYTHON\workspace2\mysite_project\manage.py startapp mysiteapp
# again run server using > python manage.py runserver

#in mysiteapp, change views.py file & mysite_project modify settings.py & urls.py

# This django sample is from edyoda tutorial
# link : https://www.edyoda.com/course/1541