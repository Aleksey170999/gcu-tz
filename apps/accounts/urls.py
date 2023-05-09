from django.urls import path

from apps.accounts.views import register_request, logout_request, login_request
app_name = 'accounts'
urlpatterns = [
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),
]