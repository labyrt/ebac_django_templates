from django.urls import reverse


def test_post_view_returns_hello_world(client):
    response = client.get(reverse("blog:post"))

    assert response.status_code == 200
    assert response.content == b"Hello World"
