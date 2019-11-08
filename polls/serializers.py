from rest_framework import serializers
from .models import Poll, Choice, Vote


class VoteSerializer(serializers.ModelSerializer):
    """
    Serializer class for Vote Model
    """
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    """
    Serializer class for Choice Model
    """
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    """
    Serializer class for Poll Model
    """
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'
