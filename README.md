# Django Intro Tutorial

![Python](https://img.shields.io/badge/Python-v3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Django](https://img.shields.io/badge/Django-v3.0.0-blue.svg?logo=Django&longCache=true&logoColor=white&colorB=a3be8c&style=flat-square&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/django-intro-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/hackersandslackers/bigquery-python-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/django-intro-tutorial.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a)](https://github.com/hackersandslackers/bigquery-python-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/django-intro-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/hackersandslackers/bigquery-python-tutorial/network)

![Django Intro Tutorial](https://res-3.cloudinary.com/hackers/image/upload/q_auto:best/v1/2019/12/django-gettingstarted.png)

A beginner's tutorial to launching a simple Django web app (part 1 of a series). This repository is the source code for the tutorial found here: https://hackersandslackers.com/getting-started-django/

## Getting Started

Installation is recommended with [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/):

```shell
$ git clone https://github.com/hackersandslackers/django-intro-tutorial.git
$ cd django-intro-tutorial
$ pipenv shell
$ pipenv update
$ python3 manage.py runserver
```

Alternatively, try installing via `setup.py`:

```shell
$ git clone https://github.com/hackersandslackers/django-intro-tutorial.git
$ cd django-intro-tutorial
$ python3 setup.py install
$ python3 manage.py runserver
```

## How to use

The scope of this tutorial covers the modest scope of serving a single page template via Django complete with styles and other static assets. Deploying this project won't result in anything glorious, as it is intended to help newcomers grasp some basic Django concepts such as:

* Installing and running Django locally
* Configuring Django settings properly
* Creating and managing “app” modules
* Serving templates via Django’s native templating system
* Styling templates with static assets
* Routing in Dango

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffees], and all coffee goes towards more content.
