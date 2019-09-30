from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30) #제목 표시 글자수 제한 30글자
    content = models.TextField() #글 내용

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)

    created= models.DateTimeField() #글 작성 시간

    author = models.ForeignKey(User, on_delete=True) #글 작성 유저

    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self): #포스터의 제목 결정
        return '{} :: {}'.format(self.title, self.author)


    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)
