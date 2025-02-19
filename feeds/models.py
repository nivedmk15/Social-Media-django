from django.db import models
import uuid
from datetime import datetime



class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post_images/")
    caption = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(blank=True,null=True,default=0)

    def __str__(self):
        return self.user
    

class Like_Post(models.Model):
    post_id = models.CharField(max_length=20)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    


class FollowManage(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.follower} following {self.user}"