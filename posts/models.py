from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now = True,auto_now_add = False)
    timestamp = models.DateTimeField(auto_now = False,auto_now_add = True)
    
    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return  reverse("detail",kwargs={"id":self.id})

class Comment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(verbose_name="Comments", default="Write your Comment")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date", null=True, blank=True)

    def __str__(self):
        return self.body

