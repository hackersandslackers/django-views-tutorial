from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


class FormClassView(FormView):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')


class CreateClassView(CreateView):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')


class UpdateClassView(UpdateView):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')


class DeleteClassView(DeleteView):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
