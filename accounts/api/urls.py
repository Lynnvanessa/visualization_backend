from accounts.api.views import (
    LoginApiView,
    RefreshJwtView,
    UserListApiView,
    UsersApiView,
)
from django.urls import path

urlpatterns = [
    path("register/", UsersApiView.as_view()),
    path("login/", LoginApiView.as_view()),
    path("refresh_jwt/", RefreshJwtView.as_view()),
    path("users/", UserListApiView.as_view()),
]
