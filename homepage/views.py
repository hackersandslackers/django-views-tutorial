from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.conf import settings


def index(request):
    context = {'template': 'homepage',
               'title': 'Django Views Tutorial',
               'description': mark_safe(settings.GITHUB_REPO)}
    return render(request, 'homepage/index.html', context)

