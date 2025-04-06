from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, LoginProcessView, RegisterProcessView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path("register/",RegisterView.as_view(),name="register"),
    path("login/process/", LoginProcessView.as_view(), name="login-process"),
    path("register/process/",RegisterProcessView.as_view(),name="register-process"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]