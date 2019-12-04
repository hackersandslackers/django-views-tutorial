from django.shortcuts import render


def index(request):
    context = {'template': 'homepage', 'title': 'My Django App'}
    return render(request, 'myapp/index.html', context)
