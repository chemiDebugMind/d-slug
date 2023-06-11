from django.contrib import admin

# Register your models here.
from .models import Articles


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)
    prepopulated_fields = {"slug":("title",)}


admin.site.register(Articles, ArticleAdmin)