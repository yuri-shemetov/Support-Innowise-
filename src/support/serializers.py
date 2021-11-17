from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tickets', 'comments']

class StatusSerializer(serializers.ModelSerializer):
    ticket_status = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    answer_status = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Status
        fields = ['id', 'name']

class TicketSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = models.Ticket
        fields = ['id', 'author',  'title', 'text', 'comments', 'status']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = models.Comment
        fields = ['id', 'author', 'text', 'ticket', 'status']