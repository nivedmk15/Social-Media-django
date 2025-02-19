from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def profile(request):
    user = request.user
    
    profile = Profile.objects.filter(user = user).first()
    
    
    if request.POST:
        if profile:
            img = request.FILES.get('profile_img')
            bio = request.POST.get('bio')
            
            if img == None:
                profile.bio = bio
                profile.save()
            else:
                profile.bio = request.POST['bio']
                profile.profile_img = img
                profile.save()
                
        else:
            img = request.FILES.get('profile_img')
            bio = request.POST['bio']
            
            
            if img == None:
                profile = Profile(user = user,id_user = user.id ,bio = bio)
                profile.save()
            else:
                profile = Profile(user = user,id_user = user.id ,bio = bio,profile_img = img)
                profile.save()


    context = {
        'profile' : profile,
        'user' : user
    }
    return render(request,'profile.html',context)



def signup(request):

    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if not User.objects.filter(email = email).first() :
                if not User.objects.filter(username = username).first():
                    user = User.objects.create_user(username = username, email = email, password = password)
                    user.save()
                    profile = Profile(user = user,id_user = user.id)
                    profile.save()
                    auth.login(request,user)
                    return redirect('profile')
                else:
                    messages.info(request,'username already exists')
            else:
                messages.info(request,'email already exists')
        else:
            messages.info(request,'password not matching')



        

        

    return render(request,'signup.html')


def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        user = auth.authenticate(username = username , password = password)
        if user:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'User name or password invalid')
            print('invalid')
    
    return render(request,'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')