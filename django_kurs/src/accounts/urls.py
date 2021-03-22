from django.urls import path
from django.contrib.auth import views
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'), 
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('profile/', views.UserUpdateView.as_view(), name='profile'),
]
