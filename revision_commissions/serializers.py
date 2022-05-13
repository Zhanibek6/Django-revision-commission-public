'''from rest_framework import serializers
from accounts.models import CustomUser
from .models import Organization

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'email']

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ['name',  'created_at']
'''
