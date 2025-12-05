# index/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Favorite, News, NewsCategory
from .forms import NewsForm


# --------------------------
# Добавление новости
# --------------------------
@login_required
def news_add(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('news_detail', nc=news.id)
    else:
        form = NewsForm()

    return render(request, 'news_add.html', {'form': form})


# --------------------------
# Главная страница
# --------------------------
def home_page(request):
    categories = NewsCategory.objects.all()
    news = News.objects.all().order_by('-date_added')

    favorite_ids = set()
    favorites_feed = []
    if request.user.is_authenticated:
        favorites_feed = (
            Favorite.objects
            .filter(user=request.user)
            .select_related('news__news_category')
            .order_by('-created_at')
        )
        favorite_ids = set(favorites_feed.values_list('news_id', flat=True))

    context = {
        'categories': categories,
        'news': news,
        'favorites_feed': favorites_feed,
        'favorite_ids': favorite_ids,
    }
    return render(request, 'home.html', context)


# --------------------------
# Новости по категории
# --------------------------
def category_page(request, nc):
    category = get_object_or_404(NewsCategory, id=nc)
    news = News.objects.filter(news_category=category).order_by('-date_added')

    favorite_ids = set()
    if request.user.is_authenticated:
        favorite_ids = set(
            Favorite.objects.filter(user=request.user, news__in=news)
            .values_list('news_id', flat=True)
        )

    context = {
        'category': category,
        'news': news,
        'favorite_ids': favorite_ids,
    }
    return render(request, 'category.html', context)


# --------------------------
# Одна новость
# --------------------------
def news_page(request, nc):
    news_item = get_object_or_404(News, id=nc)

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(
            user=request.user, news=news_item
        ).exists()

    context = {
        'news': news_item,
        'is_favorite': is_favorite,
    }
    return render(request, 'news.html', context)


@login_required
def toggle_favorite(request, nc):
    news_item = get_object_or_404(News, id=nc)

    if request.method == 'POST':
        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            news=news_item,
        )
        if not created:
            favorite.delete()

        next_url = request.POST.get('next') or request.META.get('HTTP_REFERER')
        return redirect(next_url or reverse('news_detail', args=[nc]))

    return redirect('news_detail', nc=nc)


@login_required
def favorites_page(request):
    favorites = (
        Favorite.objects
        .filter(user=request.user)
        .select_related('news__news_category')
        .order_by('-created_at')
    )
    favorite_ids = set(favorites.values_list('news_id', flat=True))

    return render(
        request,
        'favorites.html',
        {
            'favorites': favorites,
            'favorite_ids': favorite_ids,
        },
    )


# --------------------------
# Регистрация
# --------------------------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

