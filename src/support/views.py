from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User
from . import models
from . import perm

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class TicketList(generics.ListCreateAPIView):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        perm.AuthorOrReadOnly
        ]

class CommentList(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        perm.AuthorOrReadOnly
        ]