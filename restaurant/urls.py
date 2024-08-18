
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('', RestaurantViewset)

urlpatterns = [
    path('upload/', UploadCSV.as_view(), name='hello-world'),
] + router.urls
