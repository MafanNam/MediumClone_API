from django.db import InternalError
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from core_apps.articles.models import Article
from core_apps.ratings.api.exceptions import YouHaveAlreadyRated
from core_apps.ratings.models import Rating

from .serializers import RatingSerializer


class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        article_id = self.kwargs.get("article_id")
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
            except Article.DoesNotExist:
                raise ValidationError("Invalid article_ID provider")
        else:
            raise ValidationError("Article_ID is required")

        try:
            serializer.save(user=self.request.user, article=article)
        except InternalError:
            raise YouHaveAlreadyRated
