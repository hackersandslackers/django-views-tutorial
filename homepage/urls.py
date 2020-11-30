"""App URLs."""
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("function_views/", include("function_views.urls")),
    path("class_views/", include("class_views.urls")),
    path("model_views/", include("model_views.urls")),
]
