from django.contrib import admin

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
