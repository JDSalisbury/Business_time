
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()


urlpatterns = [
    path('test/', TestView.as_view(), name='hello-world'),
] + router.urls
