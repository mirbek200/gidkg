from django.db import models


class Transport(models.Model):
    where_from = models.TextField(max_length=255, null=False, blank=False)
    where_to = models.TextField(max_length=255, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    count_of_passengers = models.IntegerField(null=False, blank=False)
    type_of_transport = models.TextField(max_length=255, null=False, blank=False)
    model_of_transport = models.TextField(max_length=255, null=False, blank=False)
    departure_times = models.TimeField(null=False, blank=False)
    duration = models.TimeField(null=False, blank=False)
    distance = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    free_place = models.IntegerField(null=False, blank=False)
    