from django.contrib import admin
from .models import Post, Group, Comment, Follow


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date', 'group')
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'description')
    search_fields = ('title',)
    list_filter = ('slug',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created')
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    search_fields = ('user__username', 'following__username')
    list_filter = ('user', 'following')
    empty_value_display = '-пусто-'
