from django.contrib import admin

from .models import Tasks, Category

class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at','is_done')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'is_done')
    list_editable = ('is_done', )
    list_filter = ('is_done', 'category')
    fields = ('title', 'category', 'is_done', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Tasks, TasksAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Pink flamingo'
admin.site.site_header = 'Pink flamingo'