from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class Marks(models.Model):

    Name = models.CharField(max_length=20)
    Roll_no = models.IntegerField()
    MarksInPhysics = models.IntegerField()
    MarksInMathematics = models.IntegerField();
    MarksInChemistry = models.IntegerField();
    Total = models.IntegerField();
    Percentage = models.FloatField()

    def __str__(self):
        return self.name
    