from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import User, Message
from .forms import GuestBookForm, ViewUserProfile


@require_http_methods(["GET"])
def get_json_view(request):
    """Return request metadata to the user."""
    data = {'path': request.path,
            'received_headers': dict(request.headers.items()),
            'client_cookies': request.COOKIES}
    return JsonResponse(data)


@require_http_methods(["GET"])
def get_template_view(request):
    """Renders a page template."""
    context = {'title': 'GET Page Template View',
               'path': request.path,
               'received_headers': request.headers.items(),
               'client_cookies': request.COOKIES.items()}
    return render(request, 'simpleviews/get.html', context)


@require_http_methods(["GET", "POST"])
def form_template_view(request):
    """Handle form submission in a function-based view."""
    if request.method == 'POST':
        form = GuestBookForm(request.POST)
        if form.is_valid():
            Message.objects.create(name=form.cleaned_data.get('name'),
                                   message=form.cleaned_data.get('msg'))
            messages.success(request, 'Success!')
            return HttpResponseRedirect('form')
    else:
        form = GuestBookForm()
    context = {'title': 'Form View',
               'form': form,
               'path': request.path,
               'entries': Message.objects.all()}
    return render(request, 'simpleviews/form.html', context)


@require_http_methods(["GET", "POST"])
def user_profiles_view(request):
    """Serve objects & demonstrate get_object_or_404()."""
    all_users = User.objects.all()
    if request.method == 'POST':
        form = ViewUserProfile(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get('id')
            user = get_object_or_404(User, id=user_id)
            return HttpResponseRedirect(f'{user.id}/')
    else:
        form = ViewUserProfile()
    context = {'title': 'Users (Get or 404)',
               'form': form,
               'users': all_users,
               'path': request.path}
    return render(request, 'simpleviews/users.html', context)


@require_http_methods(["GET"])
def user_profile(request, user_id):
    # username = request.GET.get('username')
    user = User.objects.get(id=user_id)
    context = {'user': user,
               'title': f'{user.name}\'s Profile',
               'path': request.path}
    return render(request, 'simpleviews/profile.html', context)
