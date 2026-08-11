from rest_framework import serializers

from .models import Comments


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comments
        fields = ['id', 'comment', 'post', 'user', 'created_at']
        read_only_fields = ['created_at']
