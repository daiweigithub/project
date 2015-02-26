from django.contrib.auth.models import User
from rest_framework import serializers
from asm.models import Record, UserRecord


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('peakFlow', 'fev1', 'userrecords', 'path')

class UserRecordSerializer(serializers.HyperlinkedModelSerializer):
    peakFlow = serializers.ReadOnlyField(source='record.peakFlow')
    fev1 = serializers.ReadOnlyField(source='record.fev1')
    #path = serializers.ReadOnlyField(source='record.path')
    username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = UserRecord
        fields = ('username', 'peakFlow', 'fev1', 'relation', 'owner', 'record')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    record_list = UserRecordSerializer(source='userrecords', many=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'record_list')

