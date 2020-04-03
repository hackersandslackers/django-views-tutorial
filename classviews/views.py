from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, DetailView


class GenericClassView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')


class TemplateClassView(TemplateView):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')


class RedirectClassView(RedirectView):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')


class ListClassView(ListView):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')


class DetailClassView(DetailView):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')