# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db import models
import uuid
from django.core.exceptions import *

class Product(models.Model):
	name = models.CharField(max_length=200)
	product_number = models.CharField(max_length=200, blank=True, null=True)
	stock = models.IntegerField()
	price_unit = models.IntegerField()
	# unicode es para devolver el nombre prolijo de lo que es
	def __unicode__(self):
		return self.name
	def save(self, force_insert=False, force_update=False, using=None):
		if self.product_number == '0' or  self.product_number == '':
			self.product_number = uuid.uuid4().hex[:6].upper()
		super(Product, self).save()
  
class Favourite(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	# unicode es para devolver el nombre prolijo de lo que es, para devolver un id hay de returnar recursivamente
	def __unicode__(self):
		return unicode(self.id)

class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	total_price = models.IntegerField(blank=True, null=True)
	# unicode es para devolver el nombre prolijo de lo que es, para devolver un id hay de returnar recursivamente
	def __unicode__(self):
		return unicode(self.id)

	# Aclaracion, cuando se pone force_ALGO es para evitar errores de que si mandan algun valor en el atributo
	def save(self, force_insert=False, force_update=False, using=None):
		if (self.product.stock > 0):
			self.total_price = self.quantity * self.product.price_unit
			super(Order, self).save()
		else:
			if (self.product.stock - self.quantity >= 0):
				self.quantity = self.product.stock
				self.product.stock = 0
				self.product.save()
				self.total_price = self.quantity * self.product.price_unit
				super(Order, self).save()