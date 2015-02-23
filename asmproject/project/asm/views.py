#from django.shortcuts import render
from django.contrib.auth.models import User, Group
from asm.models import Record
from rest_framework import viewsets
from asm.serializers import UserSerializer, GroupSerializer, RecordSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Record to be viewed or edited.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
