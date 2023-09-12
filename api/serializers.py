from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    class Meta:
        model = Person
        fields = '__all__'
        