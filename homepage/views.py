from django.shortcuts import render


def index(request):
    context = {'template': 'homepage',
               'title': 'Django Views Tutorial',
               'description': 'Reference/cheatsheet for creating views in Django.'}
    return render(request, 'homepage/index.html', context)

