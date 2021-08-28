from .models import *
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator


def use_inventory(request, hero_id, thing_id):
    person = get_object_or_404(Paladin, id=hero_id)
    thing = get_object_or_404(Things, id=thing_id)
    print(thing)
    # person.hero_strength = person.default_strength
    # person.hero_armor = person.default_armor
    # person.hero_stamina = person.default_stamina
    # if request.method == 'POST':
    #     #fruits = request.POST.getlist('fruits')
    #     g = request.POST.get('used')
    #     print(f'тут{g}')
    #for i in person.things.all():
    if thing.used == True:
        return redirect('person_detail', hero_id)
    person.hero_armor += thing.thing_armor
    person.hero_strength += thing.thing_strength
    person.hero_stamina += thing.thing_stamina
    thing.used = True
    thing.save()
    person.save()
    return redirect('person_detail', hero_id)


def unuse_inventory(request, hero_id, thing_id):
    person = get_object_or_404(Paladin, id=hero_id)
    thing = get_object_or_404(Things, id=thing_id)
    # for i in things:
    if thing.used == False:
        return redirect('person_detail', hero_id)
    person.hero_armor -= thing.thing_armor
    person.hero_strength -= thing.thing_strength
    person.hero_stamina -= thing.thing_stamina
    thing.used = False
    thing.save()
    person.save()
    return redirect('person_detail', hero_id)


def index(request):
    person = Heroes.objects.all().values()
    paginator = Paginator(person, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page': page, 'paginator': paginator})


def person_detail(request, hero_id):
    person = get_object_or_404(Heroes, id=hero_id)
    things = person.things.all()
    # if request.method == 'POST':
    #     button_check = request.POST.get('used')
    #     print(f'тут {button_check}')
    return render(request, 'person_detail.html', {'person': person,
                                                  'things': things})
