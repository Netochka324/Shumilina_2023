from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("name", max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("name",)


class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    lust_modified = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="post_category")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("title",)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("created_on",)

# class Car(models.Model):  # многие к одному
#     new_Car = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
#
#
# class Toping(models.Model):
#     pass
#
#
# class Pizza(models.Model):  # многие ко многим
#     toppings = models.ManyToMany(Toping)
#
#
# class Place(models.Model):
#     name = models.CharField(max_length=50)
#     adress = models.CharField(max_length=40)
#
#
# class Restayrant(models.Model):
#     place=models.OneToOneField(Place)
