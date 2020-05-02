from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('create', views.CreateClassView.as_view(), name='create'),
    path('update', views.UpdateClassView.as_view(), name='update'),
    path('delete', views.DeleteClassView.as_view(), name='delete'),
    path('list', views.ListClassView.as_view(), name='list'),
    path('detail', views.DetailClassView.as_view(), name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
