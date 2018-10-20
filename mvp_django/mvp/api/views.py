from django.shortcuts import render
from mvp.api.models import *
from rest_framework.viewsets import ModelViewSet, ViewSet
from mvp.api.serializers import *
from rest_framework.response import Response

class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class ObjectViewSet(ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

class PositionViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class ObjectQuery(ViewSet):
    def list(self, request, pk):
        queryset = Object.objects.filter(flight=Flight.objects.get(pk=pk))
        serializer = ObjectSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
