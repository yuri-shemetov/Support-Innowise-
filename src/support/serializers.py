from rest_framework import serializers
from users.models import User
from . import models
from django.contrib.auth import authenticate


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

class SubscriptionSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank = False)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        all_email = models.Contact.objects.all()
        for user_email in all_email:
            if str(user.email) == str(user_email):
                raise serializers.ValidationError(
                    'You have already subscribed to our newsletter.'
                )
        return {
            'name': user.username,
            'email': user.email,
        }
    class Meta:
        model = models.Contact
        fields = ['name','email','password']