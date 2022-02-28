from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TemplateView.as_view(template_name="User/login.html"), name='login'),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(template_name="User/logout.html"), name='logout'),
]
