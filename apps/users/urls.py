from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginView, RegistrationView, AdminRegistrationView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('admin_register/', AdminRegistrationView.as_view(), name='admin_register'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]