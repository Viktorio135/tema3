from rest_framework import serializers

from .models import Dog, Breed


class DogSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для собак с дополнительным свойством breed_count
    """

    breed_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Dog
        fields = '__all__'

    def get_breed_count(self, obj):
        return obj.breed_count


class BreedSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для пород собак с дополнительным свойством count_dogs
    """

    count_dogs = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = '__all__'

    def get_count_dogs(self, obj):
        return obj.count_dogs
