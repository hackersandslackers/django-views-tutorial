from django.urls import include, path


from . import views

urlpatterns = [
    path('get', views.get_template, name='get'),
    path('form', views.form_view, name='form'),
    path('get_or_404', views.get_template, name='get_or_404'),
]
