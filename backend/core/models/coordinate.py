# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from datetime import date
import json

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import (
    Model,
)

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Gallery
from core.managers import CoordinateManager

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from django_extensions.db.models import TimeStampedModel, ActivatorModel, TitleDescriptionModel

User = get_user_model()

def coordinate_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/users/email/coordinates/<filename>
    return f'users/{instance.user.email}/coordinates/{filename}'


class Coordinate(TimeStampedModel, ActivatorModel, TitleDescriptionModel,  Model):

    '''
    Coordinate
    This is our coordinate model.
    We use this model to store user/gallery coordinate selections
    '''
    file = models.FileField(_('file'),upload_to=coordinate_directory_path, default="users/coordinates/blank_json.json")
    user = models.ForeignKey(User, verbose_name=_('user'), on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, verbose_name=_('gallery'), on_delete=models.CASCADE)

    x = models.CharField(_('x coordinate'),max_length=30,blank=True)
    y = models.CharField(_('y coordinate'),max_length=30,blank=True)
    x2 = models.CharField(_('x2 coordinate'),max_length=30,blank=True)
    y2 = models.CharField(_('y2 coordinate'),max_length=30,blank=True)

    objects = CoordinateManager()

    file_created = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Coordinates"
        ordering = ['-created']


    def create_file_name(self):
        '''
        I could get more creative but a default is fine for now.
        '''
        return "agi_coordinates"

    
    def create_json(self):
        coordinate_dict = {
            "x": self.x,
            "y": self.y,
            "x2": self.x2,
            "y2": self.y2,
        }

        if self.title:
            coordinate_dict["title"] = self.title

        blank_filename = f'{settings.MEDIA_ROOT}/users/coordinates/blank.json'
        new_filename = f'{self.create_file_name()}.json'

        if not self.file_created:
            with open(blank_filename, 'w') as f:
                json.dump(coordinate_dict ,f, indent=4, sort_keys=True, default=str)
            with open(blank_filename, "r") as f:
                self.file.save(new_filename, f)
            self.file_created = True
            self.save()


