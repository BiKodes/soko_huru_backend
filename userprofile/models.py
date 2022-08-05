import profile
from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    address = models.CharField(max_length=150, blank=True)
    postal_code = models.CharField(max_length=150, blank=True)
    county = models.CharField(max_length=150, blank=True)
    mobile = models.CharField(max_length=150, blank=True)

    def __str__(self):
        self.user.username

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])