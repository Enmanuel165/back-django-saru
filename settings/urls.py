from django.urls import path, include
from rest_framework import routers
from settings import views

router = routers.DefaultRouter()
router.register(r'settings', views.SettingsView, 'settings')

urlpatterns = [
    path("api/v1/", include(router.urls))
]
