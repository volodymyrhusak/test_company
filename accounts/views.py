from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib import auth

from django.contrib.auth import (
    authenticate,
    login
    )

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)
from accounts.serializers import (UserLoginSerializer,
                                  UserCreateSerializer,
                                  UserUpdateSerializer,
                                  UserProfileUpdateCreateSerializer, UsersSerializer)
from accounts.models import UserProfile
from django.contrib.auth.models import User

from company.permissions import IsAllowedToWrite
# Create your views here.


class UserProfileUpdateAPIView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileUpdateCreateSerializer
    lookup_field = 'user'
    permission_classes = [IsAuthenticated,IsAllowedToWrite]

    # lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save()
        # email send_email


class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'email'
    permission_classes = [IsAuthenticated,IsAllowedToWrite]

    # lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save()
        # email send_email


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,IsAllowedToWrite]


class UserProfileCreateAPIView(CreateAPIView):
    serializer_class = UserProfileUpdateCreateSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsAuthenticated,IsAllowedToWrite]


class UserLoginAPIView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, format=None, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            kwargs = {
                'username': new_data['username'],
                'password': new_data['password'],
            }
            user = auth.authenticate(**kwargs)
            extra_data={}
            auth.login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            extra_data['token'] = token.key

            return Response(extra_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UsersListAPIView(ListAPIView):
    # queryset = User.objects.all()
    serializer_class = UsersSerializer
    model = serializer_class.Meta.model
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        if self.request.user.is_staff:
            return self.model.objects.all()
        userProfile = UserProfile.objects.get(user=self.request.user)
        if userProfile.position == 'manager':
            users = UserProfile.objects.filter(company=userProfile.company).values('id')
            return self.model.objects.filter(id__in=users.values('id'))
        return self.model.objects.filter(id=self.request.user.id)


