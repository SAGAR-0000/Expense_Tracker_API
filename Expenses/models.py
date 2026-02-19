from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Expense(models.Model):
    owner=models.ForeignKey(to=User, on_delete=models.CASCADE)
    category=models.ForeignKey(to=Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField()

    def __str__(self):
        return f"{self.title}-{self.amount}"