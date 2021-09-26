import random

from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response

from Posts.serializers import *
from jadavjobs_admin.classes import Worker


@api_view(["GET"])
def api_overview(request):
    from .urls import urlpatterns
    url_list = {}
    for i in urlpatterns:
        url_list[i.name] = "/api/" + str(i.pattern)
    return Response(url_list)


@api_view(["GET"])
def link_list(request):
    posts = Post.objects.all().values("id", "name_of_the_post")
    url_list = {"posts": {}}
    serializer = PostSerializer(data=posts)
    serializer.is_valid()
    for i in serializer.validated_data:
        url_list["posts"][i["name_of_the_post"]] = f"localhost:3000/posts/{i['id']}"
    return Response(url_list)


@api_view(["GET"])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(data=posts, many=True)
    return Response(serializer.data)


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
    all = Post.objects.all()
    serializer = PostSerializer(data=all, many=True)
    id = int(random.randint(serializer.data[0]["id"], serializer.data[-1]["id"]))
    post = Post.objects.get(id=id)
    post_s = PostSerializer(post, many=False)
    return Response(post_s.data)


@api_view(["DELETE"])
def delete_all(request):
    posts = Post.objects.all().delete()
    serializer = PostSerializer(data=posts)
    serializer.is_valid()
    if serializer.validated_data == {}:
        return Response("All Objects Deleted")
    else:
        return Response(serializer.validated_data)


@api_view(["POST"])
def worker_start(request):
    path = "D:\\PROJECTS\\Python Projects\\Api Tools\\chromedriver.exe"
    url = "https://www.freejobalert.com/"
    worker = Worker(path=path, url=url)
    worker.start_application()
    worker.quit()
    return Response(worker.json)
