import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from blog.models import Post


@pytest.fixture
def author(db):
    return get_user_model().objects.create_user(
        username="autor",
        password="senha-segura-para-testes",
    )


@pytest.fixture
def published_post(author):
    return Post.objects.create(
        title="Meu primeiro post",
        author=author,
        body="Conteúdo completo do post.",
        published=True,
    )


@pytest.mark.django_db
def test_home_lists_only_published_posts(client, published_post, author):
    Post.objects.create(
        title="Rascunho invisível",
        author=author,
        body="Ainda não foi publicado.",
        published=False,
    )

    response = client.get(reverse("blog:post-list"))

    assert response.status_code == 200
    assert "index.html" in response.template_name
    assert "Meu primeiro post" in response.content.decode()
    assert "Rascunho invisível" not in response.content.decode()
    assert "About Us" in response.content.decode()


@pytest.mark.django_db
def test_post_detail_uses_template(client, published_post):
    response = client.get(
        reverse("blog:post-detail", kwargs={"pk": published_post.pk})
    )

    assert response.status_code == 200
    assert "post_detail.html" in response.template_name
    assert "Conteúdo completo do post." in response.content.decode()


@pytest.mark.django_db
def test_unpublished_post_detail_returns_404(client, author):
    draft = Post.objects.create(
        title="Rascunho",
        author=author,
        body="Conteúdo privado.",
        published=False,
    )

    response = client.get(reverse("blog:post-detail", kwargs={"pk": draft.pk}))

    assert response.status_code == 404
