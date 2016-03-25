from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PostLog(models.Model):
	when = models.DateTimeField('date created', auto_now_add = True)