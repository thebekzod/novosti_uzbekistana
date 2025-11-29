from django.db import models


class NewsCategory(models.Model):
    category_name = models.CharField(
        max_length=32,
        verbose_name='Название категории'
    )
    date_added = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class News(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Заголовок'
    )
    content = models.TextField(
        verbose_name='Основной текст'
    )
    news_category = models.ForeignKey(
        NewsCategory,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    date_added = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
