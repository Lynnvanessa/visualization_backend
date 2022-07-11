from accounts.api.serializers import UserSerializer
from accounts.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class UsersApiView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.pop("email", None)
        password = request.data.pop("password", None)
        conf_password = request.data.pop("conf_password", None)

        errors = dict()

        # check if email is provided
        if email is None:
            errors["email"] = ["Email is required."]
        else:
            if False:
                # validate email
                errors["email"] = ["Email is invalid"]
            else:
                try:
                    # check if email already exists
                    User.objects.get(email=email)
                    errors["email"] = ["A user with that email already exists."]
                except:
                    # email does not exist, so we ignore & continue
                    pass

        # check if password is provided
        if password is None:
            errors["password"] = ["Password is required."]
        # check if password matches with confirm password
        elif password != conf_password:
            errors["conf_password"] = ["Passwords do not match."]

        # check if any errors have been captured from the above validations and return if any
        if errors:
            return Response(status=400, data=errors)

        user = User.objects.create_user(email, password, **request.data)

        serializer = self.get_serializer(
            data={
                "email": email,
                "password": password,
                **request.data,
            }
        )  # gets the token serializer
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(
            {
                "user": UserSerializer(user).data,
                **serializer.validated_data,
            },
            status=status.HTTP_200_OK,
        )


class LoginApiView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        errors = dict()
        if email is None:
            errors["email"] = ["Email is required."]

        if password is None:
            errors["password"] = ["Password is required."]

        if errors:
            return Response(status=400, data=errors)

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        user = User.objects.get(email=email)
        return Response(
            {
                "user": UserSerializer(user).data,
                **serializer.validated_data,
            },
            status=status.HTTP_200_OK,
        )


class RefreshJwtView(TokenRefreshView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserListApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)
