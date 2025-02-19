from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post,Like_Post,FollowManage
from account.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


@login_required(login_url='login')
def feed(request):
    posts = Post.objects.all()
    user_profile = Profile.objects.get(user = request.user)
    

    context = {
        'posts' : posts,
        'user_profile' : user_profile
    }
    return render(request,'feeds.html',context)


def upload(request):
    if request.POST:
        user = request.user
        caption = request.POST['caption']
        
        img = request.FILES.get('image')

        if img == None:
            messages.info(request,'You need to upload image too')
            return redirect('home')

        

        post = Post(user = user.username, image = img, caption = caption)
        post.save()

        print(caption,img)
    return redirect('home')

@login_required(login_url='login')
def like_post(request):
    user = request.user.username
    post_id = request.GET['post_id']
    post = Post.objects.get(id = post_id)
    like =Like_Post.objects.filter(username = user, post_id = post_id).first()

    if like == None:
        like = Like_Post(post_id = post_id, username = user)
        like.save()
        
        post.no_of_likes += 1
        post.save()
    else:
        post.no_of_likes -= 1
        post.save()
        like.delete()
        
    return redirect('home')


@login_required(login_url='login')
def user_profile(request,username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    posts = Post.objects.filter(user = user.username)
    print(posts)
    total_posts = posts.count()
    
    if not request.user.username == user.username:
        
        follow = FollowManage.objects.filter(follower = request.user.username, user = user.username).first()
        if not follow:
            text = "FOLLOW"
        else:
            text = "UNFOLLOW"

    else:
        text = "Go to account"


    followers_count = FollowManage.objects.filter(user = username).count()
    following_count = FollowManage.objects.filter(follower = username).count()
    context = {
        'profile': profile,
        'user' : user,
        'posts' : posts,
        'total_posts': total_posts,
        'text' : text,
        'followers' : followers_count,
        'followings' : following_count

    }
    return render(request,'user_profile.html',context)

@login_required(login_url='login')
def follow(request):

    follower = request.user.username
    user = request.POST.get('user')

    if not follower == user:
        try:
            check_follow  = FollowManage.objects.get(follower = follower, user = user)
            check_follow.delete()
        except :
            manage_follow = FollowManage(follower = follower, user = user)
            manage_follow.save()
    else:
        return redirect('profile')

    return redirect('user_profile',username=user)



def search(request):
    search = request.GET.get('search')

    users = User.objects.filter(username__contains = search)
    
    user = users.first()
    

        
    context = {
        'users' : users
    }
        

    return render(request,'search.html',context)
