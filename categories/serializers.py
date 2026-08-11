from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Category
        fields = ['id', 'name', 'created_by']
