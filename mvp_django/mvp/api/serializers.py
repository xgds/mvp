from django.contrib.auth.models import User, Group
from mvp.api.models import *
from rest_framework.serializers import *

class PositionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'latitude', 'longitude')

class FlightSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = ('id', 'start', 'end')

class ObjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Object
        fields = ('id', 'time', 'name', 'flight', 'point')


    
