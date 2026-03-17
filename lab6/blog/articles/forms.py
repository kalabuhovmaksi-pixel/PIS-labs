from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, label='Заголовок')
    text = forms.CharField(widget=forms.Textarea, label='Текст')
