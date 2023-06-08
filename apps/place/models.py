from django.db import models

from apps.users.models import MyUser


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    latitude = models.CharField(max_length=255, null=False, blank=False)
    longitude = models.CharField(max_length=255, null=False, blank=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product_image/')
    description = models.CharField(max_length=255, null=False, blank=False)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)

