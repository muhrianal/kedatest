from pyexpat import model
from rest_framework import serializers 
from .models import Supplier, Material

class SupplierSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Supplier
        fields= '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class MaterialSerializerRead(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    class Meta:
        model = Material
        fields = '__all__'

