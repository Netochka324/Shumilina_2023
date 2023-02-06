from django.contrib import admin
from .models import Post, Category, Comment


admin.site.register(Post)
admin.site.register(Category, list_display=["name"])
admin.site.register(Comment)


# @admin.register(Post)
# class AdminPost(admin.ModelAdmin):
#     list_display = ["title", "body", "created_on", "categories"]


# @admin.register(Category)
# class AdminPost(admin.ModelAdmin):
#     list_display = ["author", "body", "created_on"]
