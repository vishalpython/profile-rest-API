from django.db import models
from passlib.hash import pbkdf2_sha256
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import (
AbstractBaseUser,BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(self,email,full_name,phone,password=None,is_staff=False,is_active=True,is_admin=False):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have password")
        if not full_name:
            raise ValueError("Full name must be there")
        if not phone:
            raise ValueError("Phone number must be there")
        user_obj=self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            phone=phone,

        )
        #hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)



        user_obj.set_password(password)
        user_obj.staff=is_staff
        user_obj.admin=is_admin
        user_obj.active=is_active

        user_obj.save(using=self.db)
        return user_obj

    def create_superuser(self,email,full_name,phone,password):
         user=self.create_user(
             email,
             full_name,
             phone,
             password=password,

             is_admin=True,
             is_staff=True
         )
         return user




class User(AbstractBaseUser):
    email = models.EmailField(max_length=225,unique=True)
    full_name=models.CharField(max_length=50)
    phone    = models.IntegerField(unique=True)
    active =models.BooleanField(default=True)
    staff =models.BooleanField(default=False)
    admin =models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','phone']
    object=UserManager()


    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_lable):
        return True



    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin
