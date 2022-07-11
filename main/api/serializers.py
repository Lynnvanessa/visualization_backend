from dataclasses import fields
from email.policy import default

from accounts.api.serializers import UserSerializer
from accounts.models import User
from main.models import CancerRecord, Comment
from pyexpat import model
from rest_framework import serializers


class CancerRecordSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
    )
    file = serializers.FileField()

    class Meta:
        model = CancerRecord
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
