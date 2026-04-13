from django.contrib import admin

from .models import VisitorName


@admin.register(VisitorName)
class VisitorNameAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
