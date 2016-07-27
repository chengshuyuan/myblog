from django.contrib import admin
from blog import models
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time',)


admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.BlogCategory)
admin.site.register(models.Author)
admin.site.register(models.Download)
admin.site.register(models.DownloadCategory)