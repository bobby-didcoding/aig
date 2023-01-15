# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.db import models 



class GalleryManager(models.Manager):

    def get_query_set(self):
        return self.get_queryset()

    
    def active(self):
        qs = self.get_query_set().filter(
            status=1
        )
        return qs


    def remove_user(self, user):
        qs = self.get_query_set().filter(
            users=user
        )
        for obj in qs:
            obj.users.remove(user)
            obj.save()
        return qs
