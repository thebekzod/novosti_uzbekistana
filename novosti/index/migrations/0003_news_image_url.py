from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.URLField(blank=True, help_text='Ссылка на обложку или иллюстрацию новости', verbose_name='Изображение'),
        ),
    ]
