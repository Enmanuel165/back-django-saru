from django.urls import path, include
from rest_framework import routers
from accounts import views

router = routers.DefaultRouter()
router.register(r'accounts', views.AccountView, 'accounts')

urlpatterns = [
    path("api/v1/", include(router.urls))
]
