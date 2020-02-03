from rest_framework import serializers
from backend.api_dev.models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    year = serializers.IntegerField()
    url = serializers.CharField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('year', instance.year)
        instance.url = validated_data.get('url', instance.url)
        return instance