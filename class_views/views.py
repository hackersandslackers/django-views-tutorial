"""Examples of class-based views."""
from datetime import datetime

from django.http import HttpResponseRedirect
from django.conf import settings
from django.views import View
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail

from .forms import ContactForm
from .models import PostModel


class GenericClassView(View):
    """Generic class-based view."""
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        posts = PostModel.get
        return render(request, self.template_name, {'form': 'tbh'})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class TemplateClassView(TemplateView):
    """Serve a page template."""
    template_name = 'class_views/template_class_view.html'

    # change the get method to get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        context['title'] = 'Class-based Template View'
        context['path'] = self.template_name
        return context


class ProtectedClassView(PermissionRequiredMixin, TemplateView):
    """Serve a page template to authorized users."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context


class RedirectClassView(RedirectView):
    """Permanent redirect view."""
    # https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/#redirectview
    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(PostModel, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)


class ContactView(FormView):
    """Form-based view."""
    template_name = 'class_views/contact_class_template.html'
    form_class = ContactForm
    success_url = '/success/'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

    def form_valid(self, form):
        self.send_email_message(form.cleaned_data)
        return super(ContactView, self).form_valid(form)

    @staticmethod
    def send_email_message(valid_data):
        send_mail(
            valid_data.get('subject'),
            valid_data.get('email'),
            valid_data.get('message'),
            [settings.SENDGRID_TO_EMAIL],
            fail_silently=True,
        )

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))