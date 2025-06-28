# accounts/urls.py
from django.urls import path
from .views import SignupView, CustomAuthToken, UserProfileView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]