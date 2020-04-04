from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import PostModel
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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


class ListClassView(ListView):
    # https://www.agiliq.com/blog/2017/12/when-and-how-use-django-listview/
    template_name = 'book-list.html'
    queryset = PostModel.objects.all()
    context_object_name = 'books'
    paginate_by = 10
    ordering = ['-created']

    def get_queryset(self):
        return PostModel.objects.filter(created_by=self.request.user)


class DetailClassView(DetailView):
    # https://www.agiliq.com/blog/2019/01/django-when-and-how-use-detailview/
    def get(self, request):
        # <view logic>
        return HttpResponse('result')