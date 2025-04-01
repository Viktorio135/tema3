from rest_framework import serializers

from .models import Dog, Breed


class DogSerializers(serializers.ModelSerializer):
    breed_count = serializers.SerializerMethodField()

    class Meta:
        model = Dog
        fields = '__all__'

    def get_breed_count(self, obj):
        return obj.breed_count


class BreedSerializers(serializers.ModelSerializer):
    count_dogs = serializers.SerializerMethodField()

    class Meta:
        model = Breed
        fields = '__all__'

    def get_count_dogs(self, obj):
        return obj.count_dogs
