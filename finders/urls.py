from django.urls import path, include
from rest_framework import routers
from finders import views

router = routers.DefaultRouter()
router.register(r'finders', views.FinderView, 'finders')

urlpatterns = [
    path("api/v1/", include(router.urls))
]
