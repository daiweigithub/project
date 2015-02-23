from django.contrib.auth.models import User, Group
from rest_framework import serializers
from asm.models import Record


class UserSerializer(serializers.HyperlinkedModelSerializer):
    records = serializers.HyperlinkedRelatedField(queryset=Record.objects.all(), 
							view_name='record-detail', many=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'records')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Record
        fields = ('owner', 'peakFlow', 'fev1')
