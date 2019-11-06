from django.db import models

# Create your models here.
class AvailabilityBadModel(models.Model):
	name= models.CharField(max_length=255)
	text= models.CharField(max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.CharField(max_length=20)

class AvailabilityGoodModel(models.Model):
	name= models.CharField(max_length=255)
	text= models.CharField(max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.CharField(max_length=20)

class CostBadModel(models.Model):
	name= models.CharField(max_length=255)
	text= models.CharField(max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.CharField(max_length=20)

class CostGoodModel(models.Model):
	name= models.CharField(max_length=255)
	text= models.CharField(max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.CharField(max_length=20)

class LegroomBadModel(models.Model):
	name= models.CharField(max_length=255)
	text= models.CharField(max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.CharField(max_length=20)

class LegroomGoodModel(models.Model):
	name= models.CharField(max_length=255)
	text= models.CharField(max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.CharField(max_length=20)

class TimelinessBadModel(models.Model):
	name= models.CharField(max_length=255)
	text= models.CharField(max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.CharField(max_length=20)

class TimelinessGoodModel(models.Model):
	name= models.CharField(max_length=255)
	text= models.CharField(max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.CharField(max_length=20)
