from django.urls import path

from . import views

urlpatterns = [
    path('get', views.get_template, name='get'),
    path('form', views.form_view, name='form'),
    path('get_or_404', views.get_or_404_view, name='get_or_404'),
]
