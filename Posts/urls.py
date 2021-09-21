from django.urls import path

from .views import *

urlpatterns = [
    path('', api_overview, name='api-overview'),
    path('links', link_list, name='link-list'),
    path('posts', post_list, name='post-list'),
    path('posts/<int:id>', post_detail, name='post-detail'),
    path('random-post', random_post, name='random-post'),
    path('worker', worker_start, name='worker-start'),
]
