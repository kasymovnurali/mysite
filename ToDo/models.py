from django.db import models
from django import forms
from django.conf import settings


class TodoList(models.Model):
    item = models.CharField(max_length=100)

    Activate = 'надо сделать'
    Done = 'сделано'
    Canceled = 'отменено'

    Status = (
    	(Activate, 'надо сделать'),
    	(Done, 'сделано'),
    	(Canceled, 'отменено'),)

    status = models.CharField(
    	max_length=25, 
    	choices=Status,
    	 default=Activate)

    def __str__(self):
    	return self.item