from django.contrib import admin
from django.utils.html import mark_safe

from .models import Category, Tutorial


class TutorialInline(admin.TabularInline):
    model = Tutorial
    extra = 1
    fields = (
        'name',
        'link',
        'comment',
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    inlines = (TutorialInline, )


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'tutorial_link',
        'short_comment',
    )
    list_filter = ('category', )
    
    search_fields = ('name', 'comment', )

    def tutorial_link(self, obj):
        return mark_safe(f'<a href="{obj.link}">{obj.link}</a>')
    
    def short_comment(self, obj):
        if obj.comment:
            return obj.comment[:200]
    