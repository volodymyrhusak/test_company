from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)

from accounts.models import UserProfile
from .permissions import IsAllowedToWrite
# import company.permissions

from .serializers import (
    CompanyListSerializer,
    CompanyUpdateCreateSerializer,
    CompanyDeleteSerializer)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

from company.models import CompanyModel


class CompanyDeleteAPIView(DestroyAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanyDeleteSerializer
    lookup_field = 'name'
    permission_classes = [IsAuthenticated,IsAllowedToWrite]


class CompanyUpdateAPIView(RetrieveUpdateAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanyUpdateCreateSerializer
    lookup_field = 'name'
    permission_classes = [IsAuthenticated,IsAllowedToWrite]

    def perform_update(self, serializer):
        serializer.save()


class CompanyCreateAPIView(CreateAPIView):
    serializer_class = CompanyUpdateCreateSerializer
    queryset = CompanyModel.objects.all()
    permission_classes = [IsAuthenticated,IsAllowedToWrite]

class CompanyListAPIView(ListAPIView):
    # queryset = CompanyModel.objects.all()
    serializer_class = CompanyListSerializer
    model = serializer_class.Meta.model
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        if self.request.user.is_staff:
            return self.model.objects.all()
        userProfile = UserProfile.objects.get(user=self.request.user)
        if userProfile.position == 'manager':
            # return self.model.objects.get(id=users.values('id'))
            return [userProfile.company]
        return self.model.objects.filter(id=self.request.user.id)




