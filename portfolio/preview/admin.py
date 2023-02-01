from django.contrib import admin
from .models import Project

# admin.site.register(Project)


@admin.register(Project)
class AdminPost(admin.ModelAdmin):
    list_display = ["title", "description", "image"]
