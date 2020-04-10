from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import User, Message
from .forms import GuestBookForm, ViewUserProfile


@require_http_methods(["GET"])
def get_template(request):
    context = {'title': 'Basic GET View',
               'received_headers': request.headers.items(),
               'client_cookies': request.COOKIES,
               'path': request.get_full_path()}
    return render(request, 'simpleviews/get.html', context)


@require_http_methods(["GET", "POST"])
def form_view(request):
    if request.method == 'POST':
        form = GuestBookForm(request.POST)
        if form.is_valid():
            Message.objects.create(name=form.cleaned_data.get('name'),
                                   message=form.cleaned_data.get('message'))
            messages.success(request, 'Success!')
            return HttpResponseRedirect('form')
    else:
        form = GuestBookForm()
    context = {'title': 'Form View',
               'form': form,
               'path': request.get_full_path(),
               'entries': Message.objects.all()}
    return render(request, 'simpleviews/form.html', context)


@require_http_methods(["GET", "POST"])
def users(request):
    all_users = User.objects.all()
    if request.method == 'POST':
        form = ViewUserProfile(request.POST)
        if form.is_valid():
            get_object_or_404(User, id=form.cleaned_data.get('id'))
            messages.success(request, 'You picked a valid user ID! Now try an invalid one.')
            return HttpResponseRedirect('users')
    else:
        form = ViewUserProfile()
    context = {'title': 'Users (Get or 404)',
               'form': form,
               'users': all_users,
               'path': request.get_full_path()}
    return render(request, 'simpleviews/users.html', context)
