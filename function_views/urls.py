"""Function-based view example URLs."""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("get_json/", views.get_json_view, name="get_json"),
    path("get_template/", views.get_template_view, name="get_template"),
    path("form/", views.form_template_view, name="form"),
    path("users/", views.user_profile_list_view, name="users"),
    path("users/<int:user_id>/", views.user_profile_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
