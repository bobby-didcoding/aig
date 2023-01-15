# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.db import models 



class CoordinateManager(models.Manager):

    def get_query_set(self):
        return self.get_queryset()

    
    def active(self):
        qs = self.get_query_set().filter(
            status=1
        )
        return qs