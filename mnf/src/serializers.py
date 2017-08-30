from django.contrib.auth.models import User, Group
from rest_framework import serializers
from restapp.models import *

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	groups = GroupSerializer(read_only=True, many=True)
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'groups')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'price_unit', 'product_number', 'stock')

class FavouriteSerializer(serializers.HyperlinkedModelSerializer):
	product = ProductSerializer(read_only=True)
	user = UserSerializer(read_only=True)
	class Meta:
		model = Favourite
		fields = ('id', 'product', 'user')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
	product = ProductSerializer(read_only=True)
	user = UserSerializer(read_only=True)
	class Meta:
		model = Order
		fields = ('id', 'product', 'user', 'quantity', 'total_price')