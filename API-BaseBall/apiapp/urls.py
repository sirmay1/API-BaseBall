from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("baseballs", views.BaseballView)

urlpatterns = [
    path('', include(router.urls)),
]                           