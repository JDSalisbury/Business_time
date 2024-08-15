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


class Day(RestaurantBaseModel):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Hour(RestaurantBaseModel):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    open = models.TimeField()
    close = models.TimeField()

    def __str__(self):
        return f'{self.restaurant} - {self.day} - {self.open} - {self.close}'
