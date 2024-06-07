from rest_framework import serializers
from .models import Finder

class FinderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finder
        fields = '__all__'