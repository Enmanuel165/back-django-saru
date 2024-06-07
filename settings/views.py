from rest_framework import viewsets
from .serializer import SettingsSerializer
from .models import Settings

# Create your views here.

class SettingsView(viewsets.ModelViewSet):
    serializer_class = SettingsSerializer
    queryset = Settings.objects.all()