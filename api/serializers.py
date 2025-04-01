from rest_framework import serializers

from .models import Dog, Breed


class DogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'

class BreedSerializers(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Breed
        fields = '__all__'

    def get_count(self, obj):
        return obj.count