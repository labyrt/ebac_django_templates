from django.views.generic import DetailView, ListView

from .models import Post


class PostListView(ListView):
    """Lista os posts publicados na página inicial."""

    model = Post
    template_name = "index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(published=True).select_related("author")


class PostDetailView(DetailView):
    """Exibe o conteúdo completo de um post publicado."""

    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(published=True).select_related("author")
