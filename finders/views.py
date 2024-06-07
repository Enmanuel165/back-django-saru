from rest_framework import viewsets
from .serializer import FinderSerializer
from .models import Finder

# Create your views here.

class FinderView(viewsets.ModelViewSet):
    serializer_class = FinderSerializer
    queryset = Finder.objects.all()