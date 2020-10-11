from django.shortcuts import render
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models


class UserProfileViewSets(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.object.all()
