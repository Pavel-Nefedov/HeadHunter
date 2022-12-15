from django.shortcuts import render, get_object_or_404

from .models import Article


# Create your views here.

def main(request):
    title = 'Эпик Хабр - Главная'
    article_list = Article.objects.filter(is_posted=True)

    content = {
        'title': title,
        'article_list': article_list}

    return render(request, 'mainapp/index.html', content)


def get_article(request, pk):
    title = 'Статья'
    content = {
        'title': title,
        'article': get_object_or_404(Article, pk=pk)}
    return render(request, 'mainapp/article.html', content)
