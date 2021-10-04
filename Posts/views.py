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
    serializer = PostSerializer(data=posts, many=True)
    serializer.is_valid()
    for i in serializer.validated_data:
        url_list["posts"][i["name_of_the_post"]] = f"localhost:3000/posts/{i['id']}"
    return Response(url_list)


@api_view(["GET"])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    for i, j in enumerate(posts):
        link_serializer = Links_ListSerializer(j.important_links, many=True)
        vacancy_details_list_serializer = Vacancy_ListPostSerializer(j.vacancy_details_list, many=True)
        vacancy_columns_serializer = Column_ListSerializer(j.vacancy_columns, many=True)
        qualification_list_serializer = Qual_ListSerializer(j.qualification_list, many=True)
        age_limit_list_serializer = Age_Limit_ListSerializer(j.age_limit_list, many=True)
        important_dates_serializer = Imp_Dates_ListSerializer(j.important_dates, many=True)
        application_fee_serializer = Fees_ListSerializer(j.application_fee, many=True)
        update_data = {**serializer.data[i],
                       "important_links": link_serializer.data,
                       "vacancy_details_list": vacancy_details_list_serializer.data,
                       "vacancy_columns": vacancy_columns_serializer.data,
                       "qualification_list": qualification_list_serializer.data,
                       "age_limit_list": age_limit_list_serializer.data,
                       "important_dates": important_dates_serializer.data,
                       "application_fee": application_fee_serializer.data
                       }
    return Response(update_data)


@api_view(["GET"])
def post_detail(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    link_serializer = Links_ListSerializer(posts.important_links, many=True)
    vacancy_details_list_serializer = Vacancy_ListPostSerializer(posts.vacancy_details_list, many=True)
    vacancy_columns_serializer = Column_ListSerializer(posts.vacancy_columns, many=True)
    qualification_list_serializer = Qual_ListSerializer(posts.qualification_list, many=True)
    age_limit_list_serializer = Age_Limit_ListSerializer(posts.age_limit_list, many=True)
    important_dates_serializer = Imp_Dates_ListSerializer(posts.important_dates, many=True)
    application_fee_serializer = Fees_ListSerializer(posts.application_fee, many=True)
    update_data = {**serializer.data,
                   "important_links": link_serializer.data,
                   "vacancy_details_list": vacancy_details_list_serializer.data,
                   "vacancy_columns": vacancy_columns_serializer.data,
                   "qualification_list": qualification_list_serializer.data,
                   "age_limit_list": age_limit_list_serializer.data,
                   "important_dates": important_dates_serializer.data,
                   "application_fee": application_fee_serializer.data
                   }
    return Response(update_data)


@api_view(["GET"])
def random_post(request):
    all = Post.objects.all()
    serializer = PostSerializer(all, many=True)
    id = int(random.randint(serializer.data[0]["id"], serializer.data[-1]["id"]))
    posts = Post.objects.get(id=id)
    serializer_s = PostSerializer(posts, many=False)
    link_serializer = Links_ListSerializer(posts.important_links, many=True)
    vacancy_details_list_serializer = Vacancy_ListPostSerializer(posts.vacancy_details_list, many=True)
    vacancy_columns_serializer = Column_ListSerializer(posts.vacancy_columns, many=True)
    qualification_list_serializer = Qual_ListSerializer(posts.qualification_list, many=True)
    age_limit_list_serializer = Age_Limit_ListSerializer(posts.age_limit_list, many=True)
    important_dates_serializer = Imp_Dates_ListSerializer(posts.important_dates, many=True)
    application_fee_serializer = Fees_ListSerializer(posts.application_fee, many=True)
    update_data = {**serializer_s.data,
                   "important_links": link_serializer.data,
                   "vacancy_details_list": vacancy_details_list_serializer.data,
                   "vacancy_columns": vacancy_columns_serializer.data,
                   "qualification_list": qualification_list_serializer.data,
                   "age_limit_list": age_limit_list_serializer.data,
                   "important_dates": important_dates_serializer.data,
                   "application_fee": application_fee_serializer.data
                   }
    return Response(update_data)


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
    return Response(worker.applications, status=201)
