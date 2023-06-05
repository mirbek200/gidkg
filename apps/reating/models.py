from django.db import models
from apps.place.models import Place
from apps.users.models import MyUser


class Comment(models.Model):
    post = models.ForeignKey(Place, on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    number = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
