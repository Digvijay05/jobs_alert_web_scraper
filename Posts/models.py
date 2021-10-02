from django.db import models


# Create your models here.
class Fees_List(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)
    parent = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Imp_Dates_List(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)
    date = models.CharField(max_length=400, blank=True, null=True)
    parent = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Age_Limit_List(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)
    age = models.CharField(max_length=400, blank=True, null=True)
    parent = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Column_List(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)
    parent = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Qual_List(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)
    parent = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Vacancy_List(models.Model):
    parent = models.CharField(max_length=400, blank=True, null=True)
    sub_parent = models.CharField(max_length=400, blank=True, null=True)
    row_number = models.CharField(max_length=400, blank=True, null=True)
    name = models.CharField(max_length=400, blank=True, null=True)
    rowspan = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Links_List(models.Model):
    parent = models.CharField(max_length=400, blank=True, null=True)
    name = models.CharField(max_length=400, blank=True, null=False)
    link = models.CharField(max_length=400, blank=True, null=True)
    download_file = models.FileField(upload_to=f"staticfiles/posts/uploads/%Y/%M/%D/", blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Related_Posts(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)
    link = models.CharField(max_length=400, blank=True, null=True)
    parent = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    post_heading = models.CharField(max_length=400, blank=True, null=True)
    name_of_the_post = models.CharField(max_length=400, blank=True, null=True)
    post_date = models.CharField(max_length=400, blank=True, null=True)
    latest_update = models.CharField(max_length=400, blank=True, null=True)
    vacancy = models.CharField(max_length=400, blank=True, null=True)
    brief_info = models.TextField(max_length=500, blank=True, null=True)
    table_header = models.CharField(max_length=400, blank=True, null=True)
    table_header_name = models.CharField(max_length=400, blank=True, null=True)
    advt_no = models.CharField(max_length=400, blank=True, null=True)
    application_fee = models.ManyToManyField(Fees_List)
    important_dates = models.ManyToManyField(Imp_Dates_List)
    age_limit_list = models.ManyToManyField(Age_Limit_List)
    qualification_list = models.ManyToManyField(Qual_List)
    vacancy_header = models.CharField(max_length=400, blank=True, null=True)
    vacancy_rows = models.IntegerField(blank=True, null=True)
    vacancy_columns = models.ManyToManyField(Column_List)
    vacancy_details_list = models.ManyToManyField(Vacancy_List)
    important_links = models.ManyToManyField(Links_List)
    related = models.ManyToManyField(Related_Posts)

    # tags = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.post_heading)


class Comment(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)
    email = models.EmailField(max_length=400, blank=True, null=True)
    body = models.TextField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return str(self.email)
