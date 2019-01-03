from django.db import models

# Create your models here.
class  Register(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=20)
	repeat_password = models.CharField(max_length=20)
