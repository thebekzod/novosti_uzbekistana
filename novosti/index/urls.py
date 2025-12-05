from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('category/<int:nc>/', views.category_page, name='category_detail'),
    path('news/<int:nc>/', views.news_page, name='news_detail'),
    path('news/<int:nc>/favorite/', views.toggle_favorite, name='news_favorite'),
    path('favorites/', views.favorites_page, name='favorites'),
    path('search/', views.search_news, name='search_news'),

    path('news/add/', views.news_add, name='news_add'),      # 🔹 НОВОЕ
    path('register/', views.register, name='register'),
]
