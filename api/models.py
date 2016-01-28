# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
	facebookID = models.CharField(max_length=150, blank=False, null=False)
	name = models.CharField(max_length=150, blank=False, null=False)
	username = models.CharField(max_length=150, blank=False, null=False)
	gender = models.CharField(max_length=150, blank=False, null=False)
