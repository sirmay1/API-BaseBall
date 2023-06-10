from rest_framework import serializers
from .models import Baseball


class BaseballSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Baseball
        fields =   ('id', 'name', 'division', 'city')