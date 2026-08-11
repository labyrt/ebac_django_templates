from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField("título", max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="autor",
    )
    body = models.TextField("conteúdo")
    published = models.BooleanField("publicado", default=False)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title
