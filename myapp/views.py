from django.shortcuts import render


def index(request):
    context = {'template': 'homepage',
               'title': 'My Django App',
               'description': 'You\'ve launched your first Django app! You\'re the best.'}
    return render(request, 'myapp/index.html', context)
