from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import User, GuestMessage
from .forms import GuestBookForm


@require_http_methods(["GET"])
def get_template(request):
    context = {'received_headers': request.headers.items(),
               'client_cookies': request.COOKIES,
               'path': request.get_full_path()}
    return render(request, 'simpleviews/get.html', context)


@require_http_methods(["GET", "POST"])
def form_view(request):
    if request.method == 'POST':
        form = GuestBookForm(request.POST)
        if form.is_valid():
            GuestMessage.objects.create(name=form.cleaned_data.get('name'), message=form.cleaned_data.get('message'))
            messages.success(request, 'Success!')
            return HttpResponseRedirect('form')
    else:
        form = GuestBookForm()

    context = {'form': form, 'path': request.get_full_path(), 'entries': GuestMessage.objects.all()}
    return render(request, 'simpleviews/form.html', context)


@require_http_methods(["GET"])
def get_or_404_view(request):
    obj = get_object_or_404(User, pk=1)
    context = {'user': obj}
    return render(request, 'simpleviews/form.html', context)
