from .models import Plant, Message, Owner
from rest_framework import serializers


class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ['name', 'image', 'pot', 'condition']


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['user_from ', 'user_to', 'content', 'date']


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = ['name', 'plants', 'city', 'email']








