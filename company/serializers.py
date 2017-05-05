from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    )

from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer
from company.models import CompanyModel

class CompanyUpdateCreateSerializer(ModelSerializer):
    name = CharField()
    description = CharField()

    class Meta:
        model = CompanyModel
        fields = [
            'name',
            'description',

        ]

    def validate(self, data):
        return data

    def create(self, validated_data):
        name = validated_data['name']
        description = validated_data['description']
        companyObj = CompanyModel(
            name=name,
            description=description
        )
        companyObj.save()
        return validated_data


class CompanyListSerializer(ModelSerializer):
    users = SerializerMethodField()
    class Meta:
        model = CompanyModel
        fields = [
            'users',
            'id',
            'name',
            'description',
        ]

    def get_users(self, obj):
        userModels = UserProfile.objects.filter(company=obj)
        users = UserProfileSerializer(userModels, many=True).data
        return users

class CompanyDeleteSerializer(ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = [
            'name',
            'description',
        ]