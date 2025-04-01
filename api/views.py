from rest_framework.viewsets import ModelViewSet
from django.db.models import Avg, Count, OuterRef, Subquery
from rest_framework.response import Response

from .models import Dog, Breed
from .serializers import DogSerializers, BreedSerializers


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializers

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        subquery = Dog.objects.filter(breed=OuterRef('pk')) \
            .values('breed') \
            .annotate(avg_age=Avg('age')) \
            .values('avg_age')

        query = Breed.objects.annotate(
            avg_age=Subquery(subquery)
        ).values('id', 'name', 'avg_age')

        response.data.append(query)

        return response

    def retrieve(self, request, *args, **kwargs):
        subquery = Dog.objects.filter(breed=OuterRef('breed')) \
            .values('breed') \
            .annotate(breed_count=Count('id')) \
            .values('breed_count')

        queryset = Dog.objects.filter(pk=kwargs['pk']).annotate(
            breed_count=Subquery(subquery)
        ).first()

        serializer = self.get_serializer(queryset)

        return Response(serializer.data)


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializers

    def list(self, request, *args, **kwargs):

        subquery = Dog.objects.filter(breed=OuterRef('pk')) \
            .values('breed') \
            .annotate(count_dogs=Count('id')) \
            .values('count_dogs')

        query = Breed.objects.annotate(count_dogs=Subquery(subquery))

        serializer = self.get_serializer(query, many=True)

        return Response(serializer.data)
