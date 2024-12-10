from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture']  # Add other fields as needed

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password

# Custom User serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'bio')
    
    def create(self, validated_data):
        # Create the user and hash the password
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', '')
        )
        
        # Create and return the token after user is created
        token, created = Token.objects.get_or_create(user=user)
        return {'user': user, 'token': token.key}

# Login serializer to get token from username and password
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        user = None
        try:
            user = get_user_model().objects.get(username=data['username'])
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("Invalid username or password.")
        
        if not user.check_password(data['password']):
            raise serializers.ValidationError("Invalid username or password.")
        
        # Create token for the user
        token, created = Token.objects.get_or_create(user=user)
        return {'token': token.key}

