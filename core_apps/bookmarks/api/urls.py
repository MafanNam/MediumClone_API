from django.urls import path

from .views import BookmarkCreateAPIView, BookmarkDestroyAPIView

urlpatterns = [
    path(
        "bookmark_article/<uuid:article_id>/",
        BookmarkCreateAPIView.as_view(),
        name="bookmark-create",
    ),
    path(
        "remove_bookmark/<uuid:article_id>/",
        BookmarkDestroyAPIView.as_view(),
        name="remove-bookmark",
    ),
]
