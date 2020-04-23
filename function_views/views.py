from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse

from .models import User, Message
from .forms import GuestBookForm


@require_http_methods(["GET"])
def get_json_view(request):
    """Return request metadata to the user."""
    data = {'path': request.path,
            'received_headers': dict(request.headers.items()),
            'client_cookies': request.COOKIES}
    return JsonResponse(data)


@require_http_methods(["GET"])
def get_template_view(request):
    """Render a dynamically page template."""
    context = {'title': 'GET Page Template View',
               'path': request.path,
               'received_headers': request.headers.items(),
               'client_cookies': request.COOKIES.items()}
    return render(request, 'function_views/get.html', context)


@require_http_methods(["GET", "POST"])
def form_template_view(request):
    """Create data records via form submission."""
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
    return render(request, 'function_views/form.html', context)


@require_http_methods(["GET", "POST"])
def user_profile_list_view(request):
    """Directory of user profiles."""
    user_profession = request.GET.get('profession', None)
    if user_profession:
        users = User.objects.filter(profession=user_profession)
    else:
        users = User.objects.all()
    context = {'title': 'User Profile Directory',
               'users': users,
               'path': request.path}
    return render(request, 'function_views/users.html', context)


@require_http_methods(["GET"])
def user_profile_view(request, user_id):
    """User profile page."""
    user = get_object_or_404(User, id=user_id)
    context = {'user': user,
               'title': f'{user.name}\'s Profile',
               'path': request.path}
    return render(request, 'function_views/profile.html', context)

