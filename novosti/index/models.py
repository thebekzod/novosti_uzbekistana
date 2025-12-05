from django.conf import settings
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
    image_url = models.URLField(
        verbose_name='Изображение',
        blank=True,
        help_text='Ссылка на обложку или иллюстрацию новости'
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


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorite_news'
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Новость',
        related_name='favorites'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Избранное: {self.user} — {self.news}"

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        unique_together = ('user', 'news')
