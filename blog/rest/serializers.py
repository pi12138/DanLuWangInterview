from rest_framework import serializers

from blog.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    """文章列表序列化器"""
    class Meta:
        model = Article
        fields = ('id', 'title')


class ArticleSerializer(serializers.ModelSerializer):
    """单个文章序列化器"""
    class Meta:
        model = Article
        fields = "__all__"
