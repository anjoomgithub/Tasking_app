# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # API Endpoints
    path('auth/', include('accounts.urls')),
    path('api/', include('api.urls')),

    # Frontend Pages
    # The root path will redirect to the login page
    path('', TemplateView.as_view(template_name='login.html'), name='home'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login-page'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup-page'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('admin/dashboard/', TemplateView.as_view(template_name='admin_dashboard.html'), name='admin-dashboard'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)