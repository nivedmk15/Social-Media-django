from django import template
from django.contrib.auth.models import User
from account.models import Profile
register = template.Library()

@register.simple_tag(name="userphoto")
def send_photo(username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    img = profile.profile_img.url
    return img

