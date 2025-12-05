from django.db import migrations

NEWS_ITEMS = [
    {
        "title": "Ташкент запускает ночные веломаршруты",
        "content": "Городские власти открывают освещенные велодорожки и сервисы проката, чтобы поддержать экологичный транспорт. Riders can now enjoy safer late-night routes across downtown Tashkent.",
        "category": "Город",
        "image": "/static/index/images/news1.svg",
    },
    {
        "title": "Новая солнечная электростанция в Навоийской области",
        "content": "Запущена очередная солнечная ферма мощностью 200 МВт. The project brings green energy jobs and will power over 150k households.",
        "category": "Энергетика",
        "image": "/static/index/images/news2.svg",
    },
    {
        "title": "Узбекистан и Корея открывают IT-академию",
        "content": "Совместная инициатива запускает интенсивные программы по AI и кибербезопасности. A bilingual curriculum will help students work globally.",
        "category": "Технологии",
        "image": "/static/index/images/news3.svg",
    },
    {
        "title": "Самарканд готовится к фестивалю плова",
        "content": "Мастера со всей республики приедут на ежегодный гастрономический праздник. Visitors can taste regional variations and learn recipes in Uzbek and English.",
        "category": "Культура",
        "image": "/static/index/images/news4.svg",
    },
    {
        "title": "Национальная сборная усиливает молодежный состав",
        "content": "Федерация футбола представила обновленную программу подготовки U-21. Coaches plan friendly matches abroad to boost experience.",
        "category": "Спорт",
        "image": "/static/index/images/news5.svg",
    },
    {
        "title": "Туристический маршрут по древним городам обновили",
        "content": "Семь остановок объединены единым билетом и аудиогидом на узбекском и английском языках, включая Бухару и Хиву.",
        "category": "Путешествия",
        "image": "/static/index/images/news6.svg",
    },
    {
        "title": "Финтех-стартап привлекает инвестиции",
        "content": "Узбекский сервис бесконтактных платежей объявил о раунде $12 млн. The company plans regional expansion and new features for SMEs.",
        "category": "Бизнес",
        "image": "/static/index/images/news7.svg",
    },
]


def seed_news(apps, schema_editor):
    Category = apps.get_model('index', 'NewsCategory')
    News = apps.get_model('index', 'News')

    for item in NEWS_ITEMS:
        category, _ = Category.objects.get_or_create(
            category_name=item["category"],
            defaults={"category_name": item["category"]},
        )
        News.objects.update_or_create(
            title=item["title"],
            defaults={
                "content": item["content"],
                "news_category": category,
                "image_url": item["image"],
            },
        )


def unseed_news(apps, schema_editor):
    News = apps.get_model('index', 'News')
    titles = [item["title"] for item in NEWS_ITEMS]
    News.objects.filter(title__in=titles).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('index', '0003_news_image_url'),
    ]

    operations = [
        migrations.RunPython(seed_news, reverse_code=unseed_news),
    ]
