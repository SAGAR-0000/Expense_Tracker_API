from rest_framework import serializers
from .models import Expense, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']
    
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields=['id','owner','category','title','amount','date']
        read_only_fields=['owner']