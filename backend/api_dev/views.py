from backend.api_dev.models import Article
from backend.api_dev.serializers import ArticleSerializer
from rest_framework import viewsets

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer