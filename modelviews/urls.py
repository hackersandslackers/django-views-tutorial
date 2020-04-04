from django.urls import include, path


from . import views

urlpatterns = [
    path('form', views.DetailClassView.as_view(), name='form'),
    path('create', views.CreateClassView.as_view(), name='create'),
    path('update', views.UpdateClassView.as_view(), name='update'),
    path('delete', views.DeleteClassView.as_view(), name='delete'),
]
