import pytest

from blog.models import Post


@pytest.mark.django_db
def test_create_post(django_user_model):
    author = django_user_model.objects.create_user(
        username="autor",
        password="senha-segura-123",
    )

    post = Post.objects.create(
        title="Meu primeiro post",
        author=author,
        body="Conteúdo do post criado para o teste automatizado.",
    )

    saved_post = Post.objects.get(pk=post.pk)

    assert saved_post.title == "Meu primeiro post"
    assert saved_post.author == author
    assert saved_post.body == "Conteúdo do post criado para o teste automatizado."
    assert saved_post.published is False
    assert saved_post.created_at is not None
    assert saved_post.updated_at is not None
    assert str(saved_post) == "Meu primeiro post"
