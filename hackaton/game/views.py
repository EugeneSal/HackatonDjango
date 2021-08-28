from django.http import HttpResponse
# from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404  # , redirect, render


def use_inventory(request, id=2):
    person = get_object_or_404(Paladin, id=id)
    person.hero_strength = person.default_strength
    person.hero_armor = person.default_armor
    person.hero_stamina = person.default_stamina
    for i in person.things.all():
        person.hero_armor += i.thing_armor
        person.hero_strength += i.thing_strength
        person.hero_stamina += i.thing_stamina
    person.save()
    print(person)
    return HttpResponse(person)
    # return render(request, 'posts/index.html', {
    #     'page': page, 'paginator': paginator})


def print_stats(request):
    person = get_object_or_404(Paladin, id=1)
    return HttpResponse(person)
