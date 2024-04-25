
from django.urls import path, include
from . views import ArticleDetailView, ArticleListView, ArticleCreateView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view()),
    path('articles-create/', ArticleCreateView.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]
