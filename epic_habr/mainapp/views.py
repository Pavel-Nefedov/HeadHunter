from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.timezone import now

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
        reversed_full_url_dict[value] = '/articles/'
    else:
        reversed_url_dict[value] = key
        reversed_full_url_dict[value] = f'/articles/{key}/'


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


def get_article(request, uid):
    title = 'Статья'
    content = {

        'menu': MENU_LIST,
        'url_dict': reversed_url_dict,
        'full_url_dict': reversed_full_url_dict,
        'title': title,
        'article': get_object_or_404(Article, uid=uid)}
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


def get_hub_related_articles(request, hub_en_name):
    # if not hub_en_name in hub???:
    #     return HttpResponseNotFound(f'Такой страницы у нас нет!')
    # else:

    title = f'Эпичный хабр. Статьи в хабе {hub_en_name}'
    article_list = Article.objects.filter(is_posted=True, hubs__name_slug__in=[hub_en_name])
    h1 = f'Статьи Хаба {hub_en_name}'

    content = {
        'h1': h1,
        'menu': MENU_LIST,
        'url_dict': reversed_url_dict,
        'full_url_dict': reversed_full_url_dict,
        'title': title,
        'article_list': article_list}

    return render(request, 'mainapp/index.html', content)


def delete_article(request, uid):
    article = Article.objects.get(uid=uid)
    user = request.user
    if user.username == article.author.username:
        article.deleted_at = now()
        article.save()
    #     todo: Сделать нормальное сообщение
        print('Успешно удалено')
    else:
        print(f'У Вас нет прав. Автор статьи {article.author.username}')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
