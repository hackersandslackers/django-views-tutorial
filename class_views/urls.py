"""Class-based view example URLs."""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("generic", views.GenericClassView.as_view(), name="generic_view"),
    path("template", views.TemplateClassView.as_view(), name="template_view"),
    path("list", views.ProtectedClassView.as_view(), name="protected_view"),
    path("redirect", views.RedirectClassView.as_view(), name="redirect_view"),
    path("contact", views.ContactView.as_view(), name="contact_view"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
