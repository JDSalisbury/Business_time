from django.db import models


class RestaurantBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Restaurant(RestaurantBaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
