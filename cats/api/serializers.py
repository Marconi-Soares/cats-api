from rest_framework import serializers
from .models import Cat 

class CatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat 
        fields = '__all__'
    