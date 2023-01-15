# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from datetime import date

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import (
    Model,
    BaseUserModel
)

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.managers import CustomUserManager


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/users/<email>/avatar/<filename>
    return f'users/{instance.email}/avatar/{filename}'

#This is the new custom user model
class CustomUser(AbstractBaseUser, BaseUserModel ,Model, PermissionsMixin):

    '''
    CustomUser
    This is our custom user model.
    We are extending the built-in User model in Django.
    '''

    email = models.EmailField(_('email address'),unique=True)
    dob = models.DateTimeField(_('date of birth'),blank=True,null=True)
    about = models.TextField(_('about'),max_length=500,blank=True)
    avatar = models.ImageField(_('avatar'),upload_to=user_directory_path, default="default_avatar.jpg")

    def calculate_age(self):
        born = self.dob
        today = date.today()
        try:
            birthday = born.replace(year = today.year)
    
        # raised when birth date is February 29
        # and the current year is not a leap year
        except ValueError:
            birthday = born.replace(year = today.year,
                    month = born.month + 1, day = 1)
        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year
    
    groups = models.ManyToManyField(Group,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()