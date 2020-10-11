from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, phone, password=None):
        """Create new user"""
        if not email:
            raise ValueError('User must have an email address')
        if not phone:
            raise ValueError('User must have  a phone number')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, phone, password):
        """Create and save new super user with given details"""
        user = self.create_user(email, name, phone, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for user in system"""
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    phone = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def get_full_name(self):
        """Retrieve full name of user """
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
