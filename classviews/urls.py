from django.urls import path

from . import views

urlpatterns = [
    path('generic', views.GenericClassView.as_view(), name='generic_view'),
    path('template', views.TemplateClassView.as_view(), name='template_view'),
    path('redirect', views.RedirectClassView.as_view(), name='redirect_view'),
    path('detail', views.ContactView.as_view(), name='detail_view'),
    path('list', views.ProtectedClassView.as_view(), name='list_view'),
]
