from django.db import models
from django.contrib import admin
# Create your models here.



class Plan(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    validity_days = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class AdminPlan(admin.ModelAdmin):
    model = Plan

    list_display = ('name', 'cost', 'validity_days', 'is_active')

    # def has_delete_permission(self, request, obj=None):
    #     return False

admin.site.register(Plan, AdminPlan)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    adhar_number = models.CharField(max_length=12, unique=True)
    registration_date = models.DateField(auto_now_add=True)
    mobile_number = models.CharField(max_length=10, unique=True)
    assigned_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class AdminCustomer(admin.ModelAdmin):
    model = Customer

    list_display = ('name', 'dob', 'mobile_number', 'assigned_plan', 'registration_date')
    # def has_delete_permission(self, request, obj=None):
    #     return False

admin.site.register(Customer, AdminCustomer)