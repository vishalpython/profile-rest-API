from rest_framework import serializers
from rest_framework import status
from profiles_api import models



class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize the user profile  object"""
    class Meta:
        model = models.User
        fields = ('id', 'email', 'full_name', 'phone', 'password')
        extra_kwargs = {
        "password":{
        'write_only':True,
        'style':{'input_type':'password'}
        }
        }
    def create_user(self,validated_data):
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




# class UserProfileFeedSerializer(serializers.ModelSerializer):
#     """Serialize profile feed items"""
#     class Meta:
#         model = models.ProfileFeedItems
#         fields = ('id','user_proffile','status_text','created_on')
#         extra_kwargs = {'user_proffile':{'read_only':True}}
