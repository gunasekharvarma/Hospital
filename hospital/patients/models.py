import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



# Create your models here.

class Patients(models.Model):
    patient_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    age = models.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(85)])
    blood_group = models.CharField(max_length=5)
    medical_issue = models.CharField(max_length=30)
    medication = models.CharField(max_length=30)
    recent_bill = models.IntegerField(validators=[MinValueValidator(100),MaxValueValidator(2500)])
    assigned_doctor = models.CharField(max_length=30)
    last_visited = models.DateTimeField(auto_now_add=True)
