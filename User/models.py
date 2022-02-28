from django.db import models
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from allauth.account.signals import user_logged_in
from allauth.socialaccount.models import SocialAccount

# @receiver(user_logged_in, dispatch_uid="unique")
# def user_logged_in_(request, user, **kwargs):
#     v = SocialAccount.objects.get(user=request.user)
#     print(request)
#     print("Hello Pushkar here")


# Create your models here.


class New(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    creator = models.BooleanField(default=False)
