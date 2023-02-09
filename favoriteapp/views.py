from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render

from candidateapp.models import Resume
from companyapp.models import Vacancy
from favoriteapp.models import Favorite, FavoriteCompany


"""
Избранное для кандидата
"""

@login_required
def favorites_candidate(request):
    title = "избранное"
    favorite_items = Favorite.objects.filter(user=request.user).order_by("vacancy__vacancy_name")
    content = {"title": title, "favorite_items": favorite_items, "media_url": settings.MEDIA_URL}
    return render(request, "candidateapp/favorites.html", content)


@login_required
def favorite_add_candidate(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    favorite = Favorite.objects.filter(user=request.user, vacancy=vacancy).first()

    if not favorite:
        favorite = Favorite(user=request.user, vacancy=vacancy)

    favorite.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def favorite_remove_candidate(request, pk):
    favorite_record = get_object_or_404(Favorite, pk=pk)
    favorite_record.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


"""
Избранное для компании
"""

@login_required
def favorites_company(request):
    title = "избранное компании"
    favorite_items = FavoriteCompany.objects.filter(user=request.user).order_by("resume__desired_position")
    content = {"title": title, "favorite_items": favorite_items, "media_url": settings.MEDIA_URL}
    return render(request, "companyapp/favorites.html", content)


@login_required
def favorite_add_company(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    favorite = FavoriteCompany.objects.filter(user=request.user, resume=resume).first()

    if not favorite:
        favorite = FavoriteCompany(user=request.user, resume=resume)

    favorite.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def favorite_remove_company(request, pk):
    favorite_record = get_object_or_404(FavoriteCompany, pk=pk)
    favorite_record.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
