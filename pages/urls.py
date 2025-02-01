from django.urls import path
from .views import home_view, about_view, admin_only_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about', about_view, name='about'),
    path('admin-only', admin_only_view, name='admin_only'),
]