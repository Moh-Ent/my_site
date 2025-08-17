from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('title','author', 'is_published', 'counted_views', 'created_date', 'published_date')
    list_filter = ('is_published', 'created_date' )
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)