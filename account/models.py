from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile")
    id_user = models.IntegerField()
    bio = models.CharField(max_length=100,blank=True)
    profile_img = models.ImageField(upload_to='profile_images/',default='default_pic/blank-profile-picture.png',blank=True)

    def __str__(self):
        return self.user.username
    
    


