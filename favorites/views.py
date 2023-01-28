from django.shortcuts import render, redirect


def favorites_list(request):
    context = ()
    return render(request, 'favorites/favorites-list.html', context=context)


def add_to_favorites(request, id):
    if request.method == 'POST':
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
        else:
            request.session['favorites'] = list(request.session['favorites'])

        # проверка есть ли данные в словаре (2 раза не вносить в избранное)
        item_exist = next((item for item in request.sesion['favorites'] if item['type'] == request.POST.get('type') and item['id'] == id), False)
        # print(item_exist)

        # получаем данные
        add_data = {
            'type': request.POST.get('type'),
            'id': id,
        }

        if not item_exist:
            request.session['favorites'].append(add_data)
            request.session.modified = True
    return redirect(request.POST.get('url_from'))


def remove_from_favorites(request, id):
    if request.method == 'POST':

        for item in request.session['favorites']:
            if item['id'] == id and item['type'] == request.POST.get('type'):
                item.clear()

        while {} in request.session['favorites']:
            request.session['favorites'].remove({})

        if not request.session['favorites']:
            del request.session['favorites']

        request.session.modified = True
    return redirect(request.POST.get('url_from'))


def delete_favorites(request):
    if request.session.get('favorites'):
        del request.session['favorites']

    return redirect(request.POST.get('url_from'))