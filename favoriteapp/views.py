from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render

from companyapp.models import Vacancy
from favoriteapp.models import Favorite


@login_required
def favorites(request):
    title = "избранное"
    favorite_items = Favorite.objects.filter(user=request.user).order_by("vacancy__vacancy_name")
    content = {"title": title, "favorite_items": favorite_items, "media_url": settings.MEDIA_URL}
    return render(request, "candidateapp/favorites.html", content)


@login_required
def favorite_add(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    favorite = Favorite.objects.filter(user=request.user, vacancy=vacancy).first()

    if not favorite:
        favorite = Favorite(user=request.user, vacancy=vacancy)

    favorite.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def favorite_remove(request, pk):
    favorite_record = get_object_or_404(Favorite, pk=pk)
    favorite_record.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
