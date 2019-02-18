from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User # 추천하지 않는 방식


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   # ('auth.User')로 사용해도 되지만....
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.CharField(max_length=20)     # 필수 필드, migrate 시 질문 발생
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100, db_index=True) # db_index : 필요한 필드에만 적용(migrate 필수)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
