from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Post(models.Model):
    # title = models.CharField(max_length=120)
    body = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.body

    def get_absolute_url(self):
    	return "/{pk}/".format(pk=self.pk)