from rest_framework.serializers import ModelSerializer

from Posts.models import *


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class Fees_ListSerializer(ModelSerializer):
    class Meta:

        model = Fees_List
        fields = "__all__"


class Imp_Dates_ListSerializer(ModelSerializer):
    class Meta:

        model = Imp_Dates_List
        fields = "__all__"


class Age_Limit_ListSerializer(ModelSerializer):
    class Meta:

        model = Age_Limit_List
        fields = "__all__"


class Column_ListSerializer(ModelSerializer):
    class Meta:

        model = Column_List
        fields = "__all__"


class Qual_ListSerializer(ModelSerializer):
    class Meta:

        model = Qual_List
        fields = "__all__"


class Vacancy_ListPostSerializer(ModelSerializer):
    class Meta:

        model = Vacancy_List
        fields = "__all__"


class Links_ListSerializer(ModelSerializer):
    class Meta:

        model = Links_List
        fields = "__all__"


class Related_PostsSerializer(ModelSerializer):
    class Meta:

        model = Related_Posts
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:

        model = Comment
        fields = "__all__"
