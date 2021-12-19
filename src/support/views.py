from rest_framework import generics, permissions, status, views
from . import serializers
from users.models import User
from . import models
from . import perm
from rest_framework.response import Response
from rest_framework.views import APIView
#from . service import send
from .tasks import send_letter_email


class SubscriptionPage(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.SubscriptionSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #send(serializer.instance.email)
            send_letter_email.delay(serializer.instance.email)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
