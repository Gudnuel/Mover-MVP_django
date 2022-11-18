from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
# class Customer (models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     # full_name=models.CharField(max_length=60,blank=True)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user

class Wallet (models.Model):
    name=models.CharField(max_length=5)
    balance=models.DecimalField(max_digits=19, decimal_places=10, default=0.00) # type: ignore
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Transactions (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    wallet=models.ForeignKey(Wallet, on_delete=models.CASCADE)
    TRANSACTION_CHOICE=(
        ("credit",1),
        ("debit",0)
    )
    transaction_type= models.IntegerField(choices=TRANSACTION_CHOICE, null=True)  # type: ignore
    STATUS_CHOICE=(
        ("success",2),
        ("pending",1),
        ("failed",0)
    )
    status= models.IntegerField(choices=STATUS_CHOICE, null=True)  # type: ignore
    # source_currency=models.CharField(max_length=3)
    # target_currency=models.CharField(max_length=3)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.status}"