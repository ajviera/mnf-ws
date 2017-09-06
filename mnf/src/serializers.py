from django.contrib.auth.models import User, Group
from rest_framework import serializers
from src.models import *

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	groups = GroupSerializer(read_only=True, many=True)
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'groups')

class TagSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tag
		fields = ( 'id', 'title' )

class NoteSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer( read_only = True )
	tag = TagSerializer( read_only = True )
	class Meta:
		model = Note
		fields = ( 'id', 'title', 'context', 'message', 'user', 'tag')