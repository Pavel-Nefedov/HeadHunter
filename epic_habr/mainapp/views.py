from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Article
import sys

sys.path.append('../')
from common.variables import MENU_LIST
from common.variables import URL_DICT

reversed_url_dict = {}
reversed_full_url_dict = {}
for key, value in URL_DICT.items():
    if key == '/':
        reversed_url_dict[value] = ''
        reversed_full_url_dict = 'article'
    else:
        reversed_url_dict[value] = key
        reversed_full_url_dict = f'article\\{key}'

# Create your views here.

def main(request):
    title = 'Эпик Хабр - Главная'
    article_list = Article.objects.filter(is_posted=True)
    h1 = 'Главная страница эпичного хабра'

    content = {
        'h1': h1,
        'menu': MENU_LIST,
        'url_dict': reversed_url_dict,
        'full_url_dict': reversed_full_url_dict,
        'title': title,
        'article_list': article_list}

    return render(request, 'mainapp/index.html', content)


def get_article(request, pk):
    title = 'Статья'
    content = {

        'menu': MENU_LIST,
        'url_dict': reversed_url_dict,
        'full_url_dict': reversed_full_url_dict,
        'title': title,
        'article': get_object_or_404(Article, pk=pk)}
    return render(request, 'mainapp/article.html', content)


def get_subject_related_articles(request, subject):
    if not subject in URL_DICT.keys():
        return HttpResponseNotFound(f'Такой страницы у нас нет!')
    else:

        title = f'Эпичный хабр. Статьи по теме {URL_DICT[subject]}'
        article_list = Article.objects.filter(is_posted=True, subject=URL_DICT[subject])
        h1 = f'Статьи по теме {URL_DICT[subject]}'

        content = {
            'h1': h1,
            'menu': MENU_LIST,
            'url_dict': reversed_url_dict,
            'full_url_dict': reversed_full_url_dict,
            'title': title,
            'article_list': article_list}

        return render(request, 'mainapp/index.html', content)
