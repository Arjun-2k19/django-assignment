from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Work, Artist

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()

    class Meta:
        model = Work
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True)

    class Meta:
        model = Artist
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
