from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QnA(models.Model):
    title = models.CharField(max_length=200)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    secret = models.CharField(max_length=3)

    def __str__(self):
        return self.question