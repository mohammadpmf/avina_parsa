from django.contrib import admin

from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
        model = BlogPost
        list_display = ['author', 'title', 'status', 'datetime_created', 'likes',]
        list_display_links = ['author', 'title', 'datetime_created', 'likes',]
        list_editable = ['status', ]
        ordering = ['author', 'status', 'title', 'description', 'datetime_created', 'likes',]
        search_fields = ['author', 'datetime_created', 'description',]







