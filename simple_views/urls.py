from django.urls import path

from . import views

urlpatterns = [
    path('get_json', views.get_json_view, name='get_json'),
    path('get_template', views.get_template_view, name='get_template'),
    path('form', views.form_template_view, name='form'),
    path('users', views.user_profiles_view, name='users'),
]
