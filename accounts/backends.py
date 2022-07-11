from django.contrib.auth.backends import ModelBackend

from accounts.api.serializers import UserSerializer

from .models import User


class UserBackend(ModelBackend):
    def authenticate(self, request):
        email = request.data["email"]

        try:
            user = User.objects.get(email=email)
            return UserSerializer(user).data
        except User.DoesNotExist:
            return None
