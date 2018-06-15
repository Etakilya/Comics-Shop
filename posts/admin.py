from django.contrib import admin
from .models import Post, Comment

admin.site.register(Comment)


class PostModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

admin.site.register(Post,PostModelAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved')

