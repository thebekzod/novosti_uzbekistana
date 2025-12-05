from django.contrib import admin
from .models import Favorite, News, NewsCategory


admin.site.site_header = 'Новостной портал — администрирование'
admin.site.site_title = 'Новости Узбекистана'
admin.site.index_title = 'Управление контентом'


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'date_added')
    search_fields = ('category_name',)
    ordering = ('category_name',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'news_category', 'date_added')
    list_filter = ('news_category', 'date_added')
    search_fields = ('title', 'content')
    ordering = ('-date_added',)
    autocomplete_fields = ('news_category',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'news', 'created_at')
    search_fields = (
        'user__username',
        'news__title',
    )
    list_select_related = ('user', 'news')
    ordering = ('-created_at',)


