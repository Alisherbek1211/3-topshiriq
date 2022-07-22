from rest_framework import serializers
from .models import Post,Category,Comment



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer
    comment = CommentSerializer
    class Meta:
        model = Post
        fields = '__all__'