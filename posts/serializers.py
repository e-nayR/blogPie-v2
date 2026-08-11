from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'subtitle',
            'text',
            'image',
            'category',
            'user',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']
