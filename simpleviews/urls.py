from django.urls import path

from . import views

urlpatterns = [
    path('get', views.get_template, name='get'),
    path('form', views.form_view, name='form'),
    path('users', views.users, name='users'),
]
