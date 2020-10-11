from rest_framework import serializers
from rest_framework import status
from profiles_api import models
import re



class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize the user profile  object"""
    password2 = serializers.CharField(label='Confirm Password', write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        """
        Check that both password should be same.
        """
        password = data['password']
        if data['password'] == data['password2'] and re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
            return data
        raise serializers.ValidationError("Password should be match and password must have number,special char,1-capital,1-small and min 8 char")

    def validate(self, data):
        """
        Check that email is a valid .
        """
        email = data['email']
        if re.search(r'[\w.-]+@[\w.-]+.\w+', email): # check name has more than 1 word
             return data
        raise serializers.ValidationError("Please enter valide email")



    class Meta:
        model = models.User
        fields = ('id', 'email', 'full_name', 'phone', 'password', 'password2')
        print()
        extra_kwargs = {
        "password":{
        'write_only':True,
        'style':{'input_type':'password'}
        },
        "password2":{
        'write_only':True,
        'style':{'input_type':'password'}
        }
        }


    def create(self,validated_data):
        """Create and return a new  user"""

        user = models.User.object.create_user(
        email = validated_data['email'],
        full_name = validated_data['full_name'],
        phone = validated_data['phone'],
        password = validated_data['password']
        )

        #user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
