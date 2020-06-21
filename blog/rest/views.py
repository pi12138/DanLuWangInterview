from rest_framework import viewsets
from rest_framework.response import Response

from blog.models import Article
from blog.rest.serializers import ArticleListSerializer, ArticleSerializer


class ArticleViewSet(viewsets.ViewSet):
    """
    文章视图
    """

    def list(self, request):
        articles = Article.objects.all()
        ser = ArticleListSerializer(instance=articles, many=True)

        return Response(ser.data)

    def retrieve(self, request, pk=None):
        if not pk:
            return Response({'msg': '为传入文章信息'}, status=400)

        articles = Article.objects.filter(id=pk)
        if not articles.exists():
            return Response({'msg': '文章不存在'}, status=400)

        ser = ArticleSerializer(instance=articles[0])
        return Response(ser.data)
