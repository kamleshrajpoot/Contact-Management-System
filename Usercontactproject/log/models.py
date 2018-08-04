from django.db import models

class User_info(models.Model):
	name = models.CharField(null=True, max_length=100)
	email = models.CharField(null=True, max_length=100)
	contact = models.CharField(max_length=12)
	
	def __str__(self):
		return self.name
