from rest_framework import serializers
from medics.models import Customer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'