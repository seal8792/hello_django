from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()  # 미기입시 False 지정으로 반드시 기입해야 하는 공간이 됨
    address = models.CharField(blank=True, max_length=50)   # 필수공간이 아님
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    # shop = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)   # 하나의 아이템은 무조건 하나의 샵에 포함
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # photo

    def __str__(self):
        return self.name
