# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from datetime import date

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import (
    Model,
)

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.managers import (
    GalleryManager,
)

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from django_extensions.db.models import TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel

User = get_user_model()

def gallery_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/gallery/<filename>
    return f'gallery/{filename}'


class Gallery(TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel,  Model):

    '''
    Gallery
    This is our gallery model.
    We use this model to store images and videos
    '''
    file = models.FileField(_('file'),upload_to=gallery_directory_path, default="gallery/default_image.png")

    users = models.ManyToManyField(User, verbose_name=_('users'), blank=True)

    objects = GalleryManager()

    class Meta:
        verbose_name_plural = "Gallery"
        ordering = ['-created']

    @property
    def size(self):
        return "123mb"

    @property
    def type(self):
        return "jpg"
