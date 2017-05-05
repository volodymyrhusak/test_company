# from django.contrib.auth import get_user_model
from accounts.models import UserProfile
from django.contrib.auth.models import User
from company.models import CompanyModel

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)


class UserUpdateSerializer(ModelSerializer):
    username = CharField()
    email = EmailField()

    class Meta:
        model = User
        fields = [
            'id'
            'username',
            'email',

        ]

    def validate(self, data):
        return data

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        userObj = User(
            username=username,
            email=email
        )
        userObj.save()
        return validated_data


class UserCreateSerializer(ModelSerializer):
    username = CharField()
    email = EmailField()
    password = CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        return data

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        userObj = User(
            username=username,
            email=email
        )
        userObj.set_password(password)
        userObj.save()
        return validated_data


class UserProfileUpdateCreateSerializer(ModelSerializer):
    position = CharField()
    city = CharField()

    class Meta:
        model = UserProfile
        fields = [
            'user',
            'company',
            'position',
            'city',
        ]

    def validate(self, data):
        return data

    def create(self, validated_data):
        user = validated_data['user']
        company = validated_data['company']
        city = validated_data['city']
        position = validated_data['position']
        userObj = User.objects.get(user=user)
        companyObj = CompanyModel.objects.get(name=company)
        userProfileObj = UserProfile(
            user=userObj,
            company=companyObj,
            position=position,
            city=city

        )
        userProfileObj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    email = EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

class UsersSerializer(ModelSerializer):
    userProfile = SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'userProfile'
        ]
    def get_userProfile(self, obj):
        userModels = UserProfile.objects.filter(user=obj)
        user = UserProfileSerializer(userModels, many=True).data
        return user

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user',
            'company',
            'position',
            'city',
        ]
