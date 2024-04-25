from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions

from .models import Article
from .serializers import ArticleSerializer


# Return details for the pk of article
class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Return max 10 article per page
class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]  # allows filtering articles according body of the article
    search_fields = ['body']


# You can create new article here
class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    # will assign author of the article base on logged user making request
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

