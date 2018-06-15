from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_list,
    post_detail,
    post_update,
    post_delete,
    login,
    comment,
    reg,
    user,
)

urlpatterns = [
    url(r'^$',post_list,name="post"),
    url(r'^detail/(?P<id>\d+)/$', post_detail,name="detail"),
    url(r'^update/$',post_update, name="update"),
    url(r'^delete/$',post_delete, name="delete"),
    url(r'^login/$',login, name="login"),
    url(r'^comment/$',comment, name="comment"),
    url(r'^reg/$',reg, name="reg"),
    url(r'^user/$',user, name="user"),

]
