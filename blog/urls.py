from django.urls import path

from .views import PostDetailView, PostListView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
