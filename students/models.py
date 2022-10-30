from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class University(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=50, unique=True)
    created_at_date = models.DateField()

    def __str__(self):
        return self.full_name


class Student(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    year_entered = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )

    def __str__(self):
        return self.full_name
