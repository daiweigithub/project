#from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from asm.models import Record, UserRecord
from rest_framework import viewsets, views
from asm.serializers import UserSerializer, RecordSerializer, UserRecordSerializer
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

class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Record to be viewed or edited.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def perform_create(self, serializer):
        record = serializer.save()
	userRecord = UserRecord(owner=self.request.user, record=record)
	userRecord.save()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Record.objects.all()
        else:
            return Record.objects.filter(userrecords__owner = self.request.user)

    def pre_save(self, obj):
        obj.path = self.request.FILES.get('file')

class UserRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows UserRecord to be viewed or edited.
    """
    queryset = UserRecord.objects.all()
    serializer_class = UserRecordSerializer

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
