from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("simple_views/", include("simple_views.urls")),
    path("class_views/", include("class_views.urls")),
    path("model_views/", include("model_views.urls")),
]
