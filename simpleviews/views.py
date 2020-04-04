from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import User


@require_http_methods(["GET"])
def get_template(request):
    context = {'received_headers': request.headers.items(),
               'client_cookies': request.COOKIES,
               'path': request.get_full_path()}
    return render(request, 'simpleviews/get.html', context)


@require_http_methods(["GET"])
def form_view(request):
    context = {'sent_headers': request.headers}
    return render(request, 'simpleviews/formview.html', context)


@require_http_methods(["GET"])
def form_view(request):
    obj = get_object_or_404(User, pk=1)
    context = {'user': obj}
    return render(request, 'simpleviews/formview.html', context)