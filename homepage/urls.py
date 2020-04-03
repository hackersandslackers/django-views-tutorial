from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("simpleviews/", include("simpleviews.urls")),
    path("classviews/", include("classviews.urls")),
    path("interactive/", include("interactive.urls")),
]
