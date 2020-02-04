import requests, sys, os
import acasearch

from backend.api_dev.models import Article
from backend.api_dev.serializers import ArticleSerializer
from rest_framework import viewsets
from django.http import HttpResponse

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

def index(request):
    query = request.GET.get('q', False)
    if not query:
        return HttpResponse('q parameter is empty')  

    res = acasearch.arxiv_search(query, n=1)
    prophy_id = acasearch.get_prophy_id(os.path.basename(res.get('id')))

    if not prophy_id:
        return HttpResponse('Paper not found')

    return HttpResponse(acasearch.get_citation_tree(prophy_id), depth=3)