from django.db import models

# Create your models here.
class JetblueAggregateModel(models.Model):
	tweet_id= models.BigIntegerField(default=0)
	name= models.CharField(default='', max_length=255)
	text= models.CharField(default='', max_length=1000)
	link= models.CharField(default='', max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.IntegerField()
	category= models.CharField(max_length=255)

class JetblueCondensedModel(models.Model):
	date = models.DateTimeField()
	average_prediction=models.DecimalField(max_digits=7, decimal_places=2)
	category= models.CharField(max_length=255)

class AmericanAggregateModel(models.Model):
	tweet_id= models.BigIntegerField(default=0)
	name= models.CharField(default='', max_length=255)
	text= models.CharField(default='', max_length=1000)
	link= models.CharField(default='', max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.IntegerField()
	category= models.CharField(max_length=255)

class AmericanCondensedModel(models.Model):
	date = models.DateTimeField()
	average_prediction=models.DecimalField(max_digits=7, decimal_places=2)
	category= models.CharField(max_length=255)

class UnitedAggregateModel(models.Model):
	tweet_id= models.BigIntegerField(default=0)
	name= models.CharField(default='', max_length=255)
	text= models.CharField(default='', max_length=1000)
	link= models.CharField(default='', max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.IntegerField()
	category= models.CharField(max_length=255)

class UnitedCondensedModel(models.Model):
	date = models.DateTimeField()
	average_prediction=models.DecimalField(max_digits=7, decimal_places=2)
	category= models.CharField(max_length=255)

class SpiritAggregateModel(models.Model):
	tweet_id= models.BigIntegerField(default=0)
	name= models.CharField(default='', max_length=255)
	text= models.CharField(default='', max_length=1000)
	link= models.CharField(default='', max_length=1000)
	date = models.DateTimeField()
	prediction_level=models.IntegerField()
	category= models.CharField(max_length=255)

class SpiritCondensedModel(models.Model):
	date = models.DateTimeField()
	average_prediction=models.DecimalField(max_digits=7, decimal_places=2)
	category= models.CharField(max_length=255)