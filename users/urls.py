from django.urls import path
from .views import UserCreateView, UserLoginView, UserLogoutView


urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]
