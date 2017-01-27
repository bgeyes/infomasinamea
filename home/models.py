from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Make(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return "Make: {}".format(self.name)

@python_2_unicode_compatible
class Model(models.Model):
	model_name = models.CharField(max_length=50)
	make_id = models.ForeignKey(Make, related_name="model")

	def __str__(self):
		return format(self.model_name)

@python_2_unicode_compatible
class Review(models.Model):
	review = models.CharField(max_length=500)
	year = models.IntegerField(blank=True)
	model_id = models.ForeignKey(Model, related_name="review")

	def __str__(self):
		return format(self.review)
# Create your models here.
