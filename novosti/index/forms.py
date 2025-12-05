# index/forms.py
from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image_url', 'news_category']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок новости',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст новости',
                'rows': 5,
            }),
            'image_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на изображение (опционально)',
            }),
            'news_category': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
