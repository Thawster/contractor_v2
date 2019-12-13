from django.contrib import admin
from items.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'modified')


admin.site.register(Page, PageAdmin)
