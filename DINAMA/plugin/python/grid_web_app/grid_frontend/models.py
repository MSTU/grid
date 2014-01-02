from django.db import models
from django.contrib.auth.models import User

class MathModels(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	type = models.TextField()
	content = models.TextField()
	def __unicode__(self):
		return self.name

class LoadCases(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	mathmodel = models.ForeignKey(MathModels)
	def __unicode__(self):
		return self.name

class Jobs(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	status = models.FloatField(default=0.0)
	description = models.TextField()
	def __unicode__(self):
		return self.name