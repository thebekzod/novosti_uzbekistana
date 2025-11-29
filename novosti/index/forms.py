# index/forms.py
from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'news_category']

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
            'news_category': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
