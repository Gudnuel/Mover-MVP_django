from django.contrib import admin
from .models import  Transactions, Wallet
# Register your models here.


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display= ["user","created_at","updated_at"]

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display= ["name","balance","created_at","updated_at"]

@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display= ["wallet","user","status","transaction_type","created_at","updated_at"]
