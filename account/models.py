from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class WishList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    wish_list = models.TextField(null=True)