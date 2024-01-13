# Django Views Tutorial

![Python](https://img.shields.io/badge/Python-v^3.10-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Django](https://img.shields.io/badge/Django-v^3.0.0-blue.svg?logo=Django&longCache=true&logoColor=white&colorB=a3be8c&style=flat-square&colorA=4c566a)
![MySQLClient](https://img.shields.io/badge/MySQLClient-v1.4.6-blue.svg?logo=mysql&longCache=true&logoColor=white&colorA=4c566a&colorB=bf616a&style=flat-square)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/django-views-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/hackersandslackers/django-views-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/django-views-tutorial.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a)](https://github.com/hackersandslackers/django-views-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/django-views-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/hackersandslackers/django-views-tutorial/network)

![Django Intro Tutorial](https://github.com/hackersandslackers/django-views-tutorial/blob/master/.github/django-views-1@2x.jpg?raw=true)

This repository contains source code for accompanying tutorial: [https://hackersandslackers.com/creating-django-views/](https://hackersandslackers.com/creating-django-views/)

A working demo of this source code is hosted here: [https://django.hackersandslackers.app/](https://django.hackersandslackers.app/)

## Installation

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/hackersandslackers/django-views-tutorial.git
$ cd django-views-tutorial
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 manage.py runserver
```

## Configuration

Configuration is handled by creating a **django_views_tutorial/.env** file (see **.env.example** for reference) Replace values with your own:

```.env
DEBUG=True
SECRET_KEY="yoursecretkey"
DJANGO_SETTINGS_MODULE="django_views_tutorial.settings"

DATABASE_ENGINE=django.db.backends.mysql
DATABASE_NAME=databasename
DATABASE_USER=username
DATABASE_PASSWORD=password
DATABASE_HOST=0.0.0.0
DATABASE_PORT=1234
DATABASE_CERTIFICATE="../creds/ca-certificate.crt" # (optional)
```

-----
**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffees], and all coffee goes towards more content.
