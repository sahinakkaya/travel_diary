from django.urls import path, include
from rest_framework.routers import DefaultRouter

from travels import views

router = DefaultRouter()
router.register(r'travels', views.TravelViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [path('', include(router.urls))]
