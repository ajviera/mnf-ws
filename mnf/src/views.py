# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework import viewsets
from src.models import *
from src.serializers import *

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class NoteViewSet(viewsets.ModelViewSet):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer

# class mark_as_favourite(View):
# 	def get(self, request, *args, **kwargs):
# 		try:
# 			produ = Product.objects.get(pk = kwargs['pk'])
# 			# produ = get_object_or_404(Product, pk = kwargs['pk'])
# 			new_favo = Favourite(product = produ, user = request.user)
# 			new_favo.save()
# 			return HttpResponse('Se ha marcado el producto ' + produ.name + ' como favorito, por el usuario ' + request.user.username)
# 		except Product.DoesNotExist:
# 			return HttpResponse('El producto numero ' + kwargs['pk'] + ' no existe')