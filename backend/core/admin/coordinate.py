# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin
from core.models import Coordinate


def create_json(modeladmin, request, queryset):
    for q in queryset:
        q.create_json()

@admin.register(Coordinate)
class CoordinateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','file', 'gallery')
    actions = [create_json]