from django.db import models

# Create your models here.
class urls(models.Model):
	og_link = models.CharField(max_length=1000)
	new_link = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.id}:{self.og_link} shortened to {self.new_link}"