from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Serialize all fields of the Product model
        read_only_fields = ['created_at', 'updated_at']  # Make these fields read-only
        
        