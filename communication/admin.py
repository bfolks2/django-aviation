from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('member', 'airport', 'datetime_created', 'datetime_updated')
    search_fields = ['member__user__username', 'airport__name', 'airport__icao', 'datetime_created', 'datetime_updated']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('member', 'post', 'datetime_created', 'datetime_updated')
    search_fields = ['member__user__username', 'post__member__user__name', 'airport__name', 'airport__icao',
                     'datetime_created', 'datetime_updated']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
