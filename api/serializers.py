# where data is converted to Json

from rest_framework import serializers
from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Hero
        field=('name','alias')
