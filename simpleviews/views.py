from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_safe


# Create your views here.
@require_http_methods(["GET"])
def get_template(request):
    context = {'sent_headers': request.headers}
    return render(request, 'simpleviews/get.html', context)


@require_http_methods(["GET"])
def form_view(request):
    context = {'sent_headers': request.headers}
    return render(request, 'simpleviews/formview.html', context)