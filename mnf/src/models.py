# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db import models
import uuid
from django.core.exceptions import *

class Tag(models.Model):
	title = models.CharField( max_length=200 )

	def __unicode__(self):
		return unicode(self.id)

	def save(self, force_insert=False, force_update=False, using=None):
		super(Tag, self).save()

class Note( models.Model ):
	title = models.CharField( max_length=200 )
	message = models.CharField( max_length=400, blank=True, null=True )
	user = models.ForeignKey( User, on_delete = models.CASCADE )
	tag = models.ForeignKey( Tag, on_delete = models.CASCADE )

	def __unicode__( self ):
		return self.title