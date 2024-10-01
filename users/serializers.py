from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model


class SignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        User = get_user_model() 
        try:
            user = User.objects.get(email=attrs['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Email ou mot de passe invalide")

        if not user.check_password(attrs['password']):
            raise serializers.ValidationError("Email ou mot de passe invalide")
        
        return user

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        User = get_user_model() 
        try:
            user = User.objects.get(email=attrs['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Email ou mot de passe invalide")

        if not user.check_password(attrs['password']):
            raise serializers.ValidationError("Email ou mot de passe invalide")
        
        return user
