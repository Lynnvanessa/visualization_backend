from accounts.models import ResetPassword, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
        ]


class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResetPassword
        fields = "__all__"
