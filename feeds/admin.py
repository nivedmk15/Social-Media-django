from django.contrib import admin
from . models import Post,Like_Post,FollowManage
# Register your models here.

admin.site.register(Post)
admin.site.register(Like_Post)
admin.site.register(FollowManage)