from datetime import datetime

import pytz
from django.conf import settings
from django.shortcuts import redirect

from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer, MyTokenObtainPairSerializer


class UserCreateAPIView(CreateAPIView):
    """ Эндпоинт для создания пользователя. """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class MyTokenObtainPairView(TokenObtainPairView):
    """ Эндпоинт для создания токена. """
    serializer_class = MyTokenObtainPairSerializer

    def perform_authentication(self, request):
        auth_header = request.headers.get("Authorization")
        if auth_header:
            try:
                token = auth_header.split()[1]
                user = User.objects.filter(verification_token=token).first()
                if user:
                    zone = pytz.timezone(settings.TIME_ZONE)
                    user.last_login = datetime.now(zone)
                    user.save()
            except AttributeError as e:
                print(e)


class UserListAPIView(ListAPIView):
    """ Эндпоинт просмотра списка всех пользователей. """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    """ Эндпоинт изменения пользователя. """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDestroyAPIView(DestroyAPIView):
    """ Эндпоинт удаления пользователя. """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


def user_verification(request, token):
    """ Функция верификации пользователя. """
    user = User.objects.filter(verification_token=token).first()
    if user:
        user.is_active = True
        user.save()
    return redirect("users:login")
