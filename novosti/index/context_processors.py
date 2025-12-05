from .language import LANGUAGES, resolve_language


def language_context(request):
    selected = request.GET.get('lang') or request.session.get('lang') or 'ru'
    lang = resolve_language(selected)
    request.session['lang'] = lang
    return {
        'lang': lang,
        'languages': LANGUAGES,
        'ui': LANGUAGES[lang],
    }
