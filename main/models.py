from django.db import models

# Create your models here.
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=300, null=False, blank=False)

class Material(models.Model):
    material_code = models.CharField(max_length=50, primary_key=True, unique=True, null=False, blank=False)
    material_name = models.CharField(max_length=300, null=False, blank=False)
    material_buy_price = models.IntegerField(null=False, blank=False) 
    
    MATERIAL_TYPE_CHOICES = [
        ('Fabric', 'Fabric'),
        ('Jeans', 'Jeans'),
        ('Cotton', 'Cotton'),
    ]

    material_type = models.CharField(max_length=50, choices=MATERIAL_TYPE_CHOICES, null=False, blank=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
