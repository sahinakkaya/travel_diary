from rest_framework import serializers
from travels.models import Travel
from django.contrib.auth.models import User


class TravelSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Travel
        fields = ['url', 'id', 'owner', 'title', 'date', 'place', 'notes']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    travels = serializers.HyperlinkedRelatedField(many=True,
                                                  view_name='travel-detail',
                                                  read_only=True)

    class Meta:
        model = User
        fields = ["url", "id", "username", "travels"]
