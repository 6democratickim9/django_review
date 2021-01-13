from django.db import models
from django.utils import timezone


class Post(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    productname = models.CharField(max_length=200)
    price = models.BigIntegerField()
    stock_quatity = models.BigIntegerField()
    description = models.TextField

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
