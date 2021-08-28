from rest_framework import viewsets


from .models import Message, Owner, Plant
from .serializers import MessageSerializer, OwnerSerializer
from .serializers import PlantSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('date')
    serializer_class = MessageSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all().order_by('name')
    serializer_class = OwnerSerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all().order_by('name')
    serializer_class = PlantSerializer
