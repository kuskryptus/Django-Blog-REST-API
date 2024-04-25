from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'created_date', 'edit_date', 'body', 'author']

