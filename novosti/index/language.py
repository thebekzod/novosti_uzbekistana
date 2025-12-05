LANGUAGES = {
    'ru': {
        'code': 'ru',
        'label': 'Рус',
        'nav_home': 'Лента',
        'nav_favorites': 'Избранное',
        'nav_add': 'Добавить',
        'nav_login': 'Войти',
        'nav_register': 'Регистрация',
        'search_placeholder': 'Поиск новостей...',
        'hero_title': 'Новости Узбекистана на трёх языках',
        'hero_subtitle': 'Читайте подборки, сохраняйте избранное и находите важное быстрее.',
        'categories': 'Категории',
        'feed': 'Последние публикации',
        'favorites': 'Ваши сохранённые новости',
        'read': 'Читать',
        'add_news_cta': 'Добавить новость',
    },
    'en': {
        'code': 'en',
        'label': 'Eng',
        'nav_home': 'Feed',
        'nav_favorites': 'Favorites',
        'nav_add': 'Submit',
        'nav_login': 'Sign in',
        'nav_register': 'Join',
        'search_placeholder': 'Search news...',
        'hero_title': 'Uzbekistan news — English friendly',
        'hero_subtitle': 'Curated stories with favorites and fast discovery.',
        'categories': 'Categories',
        'feed': 'Latest stories',
        'favorites': 'Your saved news',
        'read': 'Read',
        'add_news_cta': 'Add news',
    },
    'uz': {
        'code': 'uz',
        'label': 'O‘z',
        'nav_home': 'Lenta',
        'nav_favorites': 'Sevimli',
        'nav_add': 'Qo‘shish',
        'nav_login': 'Kirish',
        'nav_register': 'Ro‘yxatdan o‘tish',
        'search_placeholder': 'Yangilik qidirish...',
        'hero_title': 'Oʻzbekiston yangiliklari uch tilda',
        'hero_subtitle': 'Tanlangan maqolalar, sevimlilar va qulay izlash.',
        'categories': 'Toifalar',
        'feed': 'So‘nggi maqolalar',
        'favorites': 'Saqlanganlar',
        'read': 'O‘qish',
        'add_news_cta': 'Yangilik qo‘shish',
    },
}


DEFAULT_LANG = 'ru'


def resolve_language(code: str) -> str:
    if code in LANGUAGES:
        return code
    return DEFAULT_LANG
