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
    serializer_class = serializers.TicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return models.Ticket.objects.all()
        elif user.is_authenticated:
            return models.Ticket.objects.filter(author=user)

        

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        perm.AuthorOrReadOnly
        ]

class CommentList(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return models.Comment.objects.all()
        elif user.is_authenticated:
            ticket = models.Ticket.objects.filter(author=user)
            commit_for_me=[]
            for i in ticket:
                commit_for_me += models.Comment.objects.filter(ticket=i)
            return commit_for_me

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        perm.AuthorOrReadOnly
        ]
