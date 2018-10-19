from django.db import models

class Users(models.Model):
		userid = models.CharField(max_length=100)
		username = models.CharField(max_length=100)