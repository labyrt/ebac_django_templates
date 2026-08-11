from django.http import HttpResponse
from django.views import View


class PostView(View):
    """Exibe a resposta inicial da área de posts."""

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World")
