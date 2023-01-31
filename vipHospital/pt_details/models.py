
from django.db import models

# Create your models here.
class my(models.Model):
	First_Name = models.CharField(max_length=20)
	Last_Name = models.CharField(max_length=20)
	Father_Name = models.CharField(max_length=30)
	DOB = models.CharField(max_length=20)
	Gender = models.CharField(max_length=10)
	Height = models.IntegerField()
	Weight = models.IntegerField()
	Marital_Status = models.CharField(max_length=10)
	Email_Id = models.CharField(max_length=50)
	Mob_No = models.IntegerField()
	Address = models.TextField(max_length=500)
	City = models.CharField(max_length=20)
	Pin_Code = models.IntegerField()
	State = models.CharField(max_length=20)
	Country = models.CharField(max_length=20)

	def __str__(self):
		return self.First_Name