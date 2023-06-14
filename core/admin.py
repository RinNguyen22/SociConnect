from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'caption', 'created_at', 'no_of_likes']


admin.site.register(Profile)
admin.site.register(Post, PostAdmin)
admin.site.register(LikePost)
admin.site.register(FollowersCount)