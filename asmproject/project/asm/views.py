#from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from asm.models import Record
from rest_framework import viewsets
from asm.serializers import UserSerializer, GroupSerializer, RecordSerializer
from rest_framework import permissions
from asm.permissions import IsOwner
from rest_framework.parsers import FileUploadParser

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id = self.request.user.id)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = (permissions.IsAdminUser,)

class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Record to be viewed or edited.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    #permission_classes = (IsOwner,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Record.objects.all()
        else:
            return Record.objects.filter(owner = self.request.user)

"""
class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)
"""
