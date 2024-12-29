from rest_framework import viewsets, permissions
from .models import CustomToken
from .serializers import CustomTokenSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = CustomToken.objects.all()
    serializer_class = CustomTokenSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return CustomToken.objects.filter(user=self.request.user)
