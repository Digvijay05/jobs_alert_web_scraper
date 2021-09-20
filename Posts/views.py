from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response


@api_view(["GET"])
def api_overview(request):
    from .urls import urlpatterns
    url_list = {}
    for i in urlpatterns:
        print(i.pattern)
        url_list[i.pattern] = i.name
    return Response(url_list)
