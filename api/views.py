from rest_framework.viewsets import ModelViewSet
from django.db.models import Avg, Count, OuterRef, Subquery
from rest_framework.response import Response

from .models import Dog, Breed
from .serializers import DogSerializers, BreedSerializers

class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializers


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializers

