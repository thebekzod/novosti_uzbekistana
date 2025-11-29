# index/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import NewsCategory, News
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

    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'home.html', context)


# --------------------------
# Новости по категории
# --------------------------
def category_page(request, nc):
    category = get_object_or_404(NewsCategory, id=nc)
    news = News.objects.filter(news_category=category).order_by('-date_added')

    context = {
        'category': category,
        'news': news,
    }
    return render(request, 'category.html', context)


# --------------------------
# Одна новость
# --------------------------
def news_page(request, nc):
    news_item = get_object_or_404(News, id=nc)

    context = {
        'news': news_item,
    }
    return render(request, 'news.html', context)


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
