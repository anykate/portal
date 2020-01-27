from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'members'

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
