from rest_framework import serializers

from animal.models import Animal


class AnimalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('__all__')