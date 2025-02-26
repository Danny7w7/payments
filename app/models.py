from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Companies(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=20, decimal_places=6)

    def __str__(self):
        return self.name

class Users(AbstractUser):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username

class Services(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=4)
    description = models.TextField()

    def __str__(self):
        return self.name

class Subscriptions(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.company.name} - {self.service.name}'

class Transactions(models.Model):
    TRANSACTION_TYPES = (
        ('recarga', 'Recarga'),
        ('descuento', 'Descuento'),
    )

    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.company.name} - {self.type} - {self.amount}'