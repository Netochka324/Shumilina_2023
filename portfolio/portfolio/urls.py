from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", views.home),
    # path('reverse/', views.reverse, name= 'reverse'),
    path("", include("preview.urls")),
]
