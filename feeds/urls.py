from django.urls import path
from . import views

urlpatterns = [
    path('',views.feed,name='home'),
    path('upload/',views.upload,name="upload"),
    path('like_post/',views.like_post,name='like_post'),
    path('user_profile/<str:username>/',views.user_profile,name="user_profile"),
    path('follow/',views.follow,name='follow'),
    path('search/',views.search,name='search'),
    
]
