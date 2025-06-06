from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'upvotes', 'created_at']
        read_only_fields = ['author', 'upvotes']
