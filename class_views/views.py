from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import FormView
from .forms import ContactForm
from .models import PostModel
from datetime import datetime


class GenericClassView(View):
    form_class = ContactForm
    initial = {'key': 'value'}
    template_name = 'class_views/form_class_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class TemplateClassView(TemplateView):
    # change the get method to get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context


class ProtectedClassView(PermissionRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context


class RedirectClassView(RedirectView):
    # https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/#redirectview
    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(PostModel, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)


class ContactView(FormView):
    template_name = 'class_views/contact_class_template.html'
    form_class = ContactForm
    success_url = '/contact/'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Form'
        context['path'] = self.template_name
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))