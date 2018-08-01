from django.contrib import admin
from blog import models

@admin.register(models.BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name', ]


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'blog_type', 'create_time', 'update_time', ]


