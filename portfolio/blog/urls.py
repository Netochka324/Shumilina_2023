from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.blog_index, name='blog_index'),
    path("<int:pk>/", views.blog_detail, name='blog_detail'),
    path("category_1/", views.blog_category_1, name='blog_category_1'),
    path("category_2/", views.blog_category_2, name='blog_category_2'),
    path("category_3/", views.blog_category_3, name='blog_category_3'),
    path("category/<int:pk>/", views.blog_category_0, name='blog_category_0')
]