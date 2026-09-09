from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length = 8)
    password2 = serializers.CharField(write_only=True, min_length = 8)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise ValueError({'password':'Password does not match!'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(password=password, **validated_data)