from django.db import models
from django.contrib.auth.models import User
# from user.models import User

# # # Create your models here.
# # class Photo(core_models.TimeStampedModel):
# #     """Photo Model Definition"""
# #     caption = models.CharField(max_length=80)
# #     file = models.ImageField(upload_to="room_photos",)
# #     room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)
# #     def __str__(self):
# #         return self.caption
#
class Community(models.Model):
    # title = models.CharField(max_length=30,null=True,blank=True)
    content = models.CharField(max_length=800)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=3)
    region = models.CharField(max_length=20)
    # img_url=models

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.ForeignKey(Community,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    comment=models.CharField(max_length=200)

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=80)