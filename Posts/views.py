from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response

from Posts.models import *


@api_view(["GET"])
def api_overview(request):
    from .urls import urlpatterns
    url_list = {}
    for i in urlpatterns:
        url_list[str(i.pattern)] = i.name
    return Response(url_list)


@api_view(["GET"])
def link_list(request):
    from .urls import urlpatterns
    url_list = {}
    print(urlpatterns[0].pattern)
    for i in urlpatterns:
        url_list[str(i.pattern)] = i.name
    return Response(url_list)


@api_view(["GET"])
def post_list(request):
    from .urls import urlpatterns
    url_list = {}
    print(urlpatterns[0].pattern)
    for i in urlpatterns:
        url_list[str(i.pattern)] = i.name
    return Response(url_list)


@api_view(["GET"])
def post_detail(request):
    from .urls import urlpatterns
    url_list = {}
    print(urlpatterns[0].pattern)
    for i in urlpatterns:
        url_list[str(i.pattern)] = i.name
    return Response(url_list)


@api_view(["GET"])
def random_post(request):
    from .urls import urlpatterns
    url_list = {}
    print(urlpatterns[0].pattern)
    for i in urlpatterns:
        url_list[str(i.pattern)] = i.name
    return Response(url_list)


@api_view(["POST"])
def worker_start(request):
    posts = Post.objects.all()
    post_list = []
    return Response(post_list)
