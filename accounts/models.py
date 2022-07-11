from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db import models


class UserManager(UserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = User.objects.create(
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=25, null=True, unique=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = UserManager()


class ResetPassword(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    code = models.IntegerField(null=False, blank=False)
    expiry = models.DateTimeField(null=False, blank=False)
    issue_date = models.DateField(null=False, blank=False, auto_now=True)
