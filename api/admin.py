from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text', )
    list_filter = ('pub_date', )
    empty_value_display = '--пусто--'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created')
    list_filter = ('created', )
    search_fields = ('text', )


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_fields = ('user__following', )
