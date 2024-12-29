from rest_framework import serializers
from .models import CustomToken

class CustomTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomToken
        fields = ('key', 'user', 'created', 'expires', 'is_active', 'description')
        read_only_fields = ('key', 'created')
